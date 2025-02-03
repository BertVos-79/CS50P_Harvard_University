"""
PROJECT:  SlideSift – The Smart Way to Filter Slides.

A Python program that:
1. Provides a GUI to filter slides in a PDF.
2. Uses a rule-based approach to merge incremental "builds."
3. Exports a filtered PDF.

Author: Bert Vos
Date: 2025-02-04
"""

import subprocess
import sys

# Dictionary of required libraries with their versions
required_libraries = {
    "PyMuPDF": "1.22.5",
    "PyPDF2": "3.0.1",
    "reportlab": "3.6.12"
}

def install_missing_libraries():
    """
    Ensures all required dependencies are installed.
    If a library is missing, prompts the user for installation.
    """
    for package, version in required_libraries.items():
        try:
            if package == "PyMuPDF":
                __import__("fitz")  # PyMuPDF is imported as fitz
                # funny blog on historical roots of this rarity: https://artifex.com/blog/pymupdf-1.24.3-and-farewell-to-fitz
            else:
                __import__(package.lower())
        except ImportError:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", f"{package}=={version}"]
            )


# Install missing libraries
install_missing_libraries()

# Import libraries
from dataclasses import dataclass
import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # PyMuPDF
import PyPDF2
from io import BytesIO
import reportlab.pdfgen.canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch


def main():
    """
    Launches a GUI for selecting an input PDF, processing it using a rule-based approach,
    and saving a filtered output PDF.
    """
    root = tk.Tk()
    root.title("SlideSift – The Smart Way to Filter Slides.")

    pdf_input_path_var = tk.StringVar(root)
    output_file_path_var = tk.StringVar(root)

    def select_input():
        selected = filedialog.askopenfilename(
            title="Select Input PDF", filetypes=[("PDF files", "*.pdf")]
        )
        if selected:
            pdf_input_path_var.set(selected)

    def select_output():
        selected = filedialog.asksaveasfilename(
            title="Save Filtered PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
        )
        if selected:
            output_file_path_var.set(selected)

    def process_pdf():
        pdf_input_path = pdf_input_path_var.get()
        output_pdf_path = output_file_path_var.get()
        if not pdf_input_path or not output_pdf_path:
            messagebox.showerror("Error", "Please select both input and output PDFs.")
            return

        # Filter the PDF with the rule-based approach
        filtered_slides = filter_slides_rule_based(pdf_input_path)

        # Generate filtered PDF
        write_filtered_pdf(pdf_input_path, output_pdf_path, filtered_slides)

        # Display confirmation message
        messagebox.showinfo("Done", f"Created: {output_pdf_path}")

    # Set GUI elements
    tk.Label(root, text="Input PDF:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    tk.Entry(root, textvariable=pdf_input_path_var, width=40).grid(
        row=0, column=1, padx=5, pady=5
    )
    tk.Button(root, text="Browse", command=select_input).grid(
        row=0, column=2, padx=5, pady=5
    )

    tk.Label(root, text="Output PDF:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    tk.Entry(root, textvariable=output_file_path_var, width=40).grid(
        row=1, column=1, padx=5, pady=5
    )
    tk.Button(root, text="Browse", command=select_output).grid(
        row=1, column=2, padx=5, pady=5
    )

    tk.Button(root, text="Process", command=process_pdf).grid(
        row=2, column=0, columnspan=3, pady=10
    )

    # Start GUI event loop
    root.mainloop()


@dataclass
class SlideInfo:
    """
    Structured representation of slide content.
    Stores extracted information from `parse_page()` and serves as input to `is_extension()`.
    """

    first_line: str
    remaining_lines: list[str]
    image_count: int


def parse_page(fitz_page: fitz.Page) -> SlideInfo:
    """
    Extracts structured information from a PyMuPDF page.

    Parameters:
        fitz_page (fitz.Page): A page object from PyMuPDF.

    Returns:
        SlideInfo: An object containing:
          - first_line (str): The first non-empty line of text.
          - remaining_lines (list[str]): The remaining lines of text.
          - image_count (int): The number of images found on the slide.
    """
    # Extract text from PDF
    raw_text = fitz_page.get_text() or ""  # Ensure raw text is always string
    lines = [ln.strip() for ln in raw_text.splitlines() if ln.strip()]

    # Extract first line and remaining lines
    if len(lines) == 0:
        first_line = ""
        remaining_lines = []
    else:
        first_line = lines[0]
        remaining_lines = lines[1:]

    # Count images
    img_list = fitz_page.get_images(full=True)
    image_count = len(img_list)

    # Return structured page information
    return SlideInfo(first_line, remaining_lines, image_count)


def is_extension(old_slide: SlideInfo, new_slide: SlideInfo) -> bool:
    """
    Determines whether `new_slide` is an incremental build of `old_slide`.

    Parameters:
        old_slide (SlideInfo): The previous slide.
        new_slide (SlideInfo): The new slide.

    Returns:
        bool: True if `new_slide` is an incremental build of `old_slide`, otherwise False.

    Conditions for an incremental build:
      1) The slides have the same first line.
      2) new_slide contains all lines from old_slide + possibly more.
      3) new_slide has at least as many images as old_slide.
    """
    # Check whether first lines match
    if new_slide.first_line != old_slide.first_line:
        return False

    # Check whether new slide has as many remaining lines as previous slide
    if len(new_slide.remaining_lines) < len(old_slide.remaining_lines):
        return False

    # Check whether remaining lines previous slide are sequentially contained in new slide
    for i, line in enumerate(old_slide.remaining_lines):
        if i >= len(new_slide.remaining_lines) or line != new_slide.remaining_lines[i]:
            return False

    # Check whether new slide has at least as many images as previous slide
    if new_slide.image_count < old_slide.image_count:
        return False

    # If all checks pass confirm new slide is incremental build of previous slide
    return True


@dataclass
class FilteredSlides:
    """
    Encapsulates the indices of slides that should be retained in the final PDF.
    Used as the return type for `filter_slides_rule_based()`.
    """

    kept_indices: list[int]


def filter_slides_rule_based(pdf_input_path: str) -> FilteredSlides:
    """
    Reads the PDF from `pdf_input_path`, merges partial slides according to `is_extension()`,
    and returns a list of final page indices.

    Parameters:
        pdf_input_path (str): Path to the input PDF.

    Returns:
        FilteredSlides: An object containing `kept_indices` (list of retained slide indices).
    """
    # Open input PDF
    doc = fitz.open(pdf_input_path)

    # Initialize variables
    kept_indices = []
    pending_data = None
    pending_index = None

    # Iterate through PDF slides
    for i, fitz_page in enumerate(doc):
        new_slide_info = parse_page(fitz_page)

        # Set data and index for first slide
        if pending_data is None:
            pending_data = new_slide_info
            pending_index = i
            continue

        # Check for incremental builds
        if is_extension(pending_data, new_slide_info):
            # if yes: update data and index previous slide
            pending_data = new_slide_info
            pending_index = i
        else:
            # if no: store index previous slide, update data with new slide
            kept_indices.append(pending_index)
            pending_data = new_slide_info
            pending_index = i

    # Add index last processed slide
    if pending_index is not None:
        kept_indices.append(pending_index)

    doc.close()
    return FilteredSlides(kept_indices)


def write_filtered_pdf(
    input_pdf_path: str, output_pdf_path: str, filtered_slides: FilteredSlides
):
    """
    Reads the original input PDF, extracts pages with indices specified in `filtered_slides.kept_indices`,
    and writes a new filtered PDF.

    Parameters:
        input_pdf_path (str): Path to the original PDF.
        output_pdf_path (str): Path for the filtered output PDF.
        filtered_slides (FilteredSlides): Object containing indices of slides to retain.
    """
    # Open input PDF, create output PDF
    reader = PyPDF2.PdfReader(input_pdf_path)
    writer = PyPDF2.PdfWriter()

    # Add selected pages to output PDF
    for idx in filtered_slides.kept_indices:
        writer.add_page(reader.pages[idx])

    # Write out output PDF
    with open(output_pdf_path, "wb") as out_file:
        writer.write(out_file)


if __name__ == "__main__":
    main()
