![CS50P Banner](images/slideshift.webp)

# SlideSift - The Smart Way to Filter Slides

## Video Demo 

https://youtu.be/i_GIHZEYEjk

## Description

**SlideSift** is a Python-based tool that intelligently filters incremental builds from slide-based PDFs. It allows users to:

- Select an input PDF
- Process it through a rule-based filtering approach
- Export a refined version with redundant slides removed

The program is particularly useful for cleaning up presentation slides exported as PDFs, where minor incremental builds lead to excessive redundancy.

The software provides an intuitive **Graphical User Interface (GUI)** to facilitate file selection and processing, making it accessible even for users without programming experience. Internally, it applies a set of predefined rules to detect incremental builds and determine whether a new slide is an extension of a previous one. By doing so, it ensures that only the most complete versions of slides are retained in the final output.

## Features

- **Graphical User Interface (GUI):** Users can select input and output PDF files through an easy-to-use GUI.
- **Automated Incremental Slide Filtering:** The program analyzes textual content and images to determine whether a slide is merely a small extension of the previous one.
- **Efficient PDF Processing:** Uses `PyMuPDF (Fitz)` and `PyPDF2` to extract and manipulate PDFs efficiently.
- **Custom Filtering Rules:** The script follows a rule-based approach to determine when a slide should be removed as redundant.
- **Test-Driven Development:** Includes comprehensive unit tests to ensure accuracy and reliability.

## Files and Functionality

### `project.py`

This is the main script that drives the entire application. It contains:

- `install_missing_libraries()`: Ensures all required dependencies are installed before execution.
- `main()`: Initializes and runs the GUI.
- `parse_page(fitz_page: fitz.Page) -> SlideInfo`: Extracts structured text and image information from each slide.
- `is_extension(old_slide: SlideInfo, new_slide: SlideInfo) -> bool`: Determines whether a new slide is just an incremental build of a previous slide.
- `filter_slides_rule_based(pdf_input_path: str) -> FilteredSlides`: Reads the PDF, applies filtering rules, and identifies slides to keep.
- `write_filtered_pdf(input_pdf_path: str, output_pdf_path: str, filtered_slides: FilteredSlides)`: Writes a new PDF file with only the selected slides.

### `test_project.py`

This file contains unit tests for key functions using `pytest`. It includes:

- **Tests for `parse_page()`**: Ensures correct extraction of text and images.
- **Tests for `is_extension()`**: Validates the detection of incremental builds.
- **Tests for `filter_slides_rule_based()`**: Simulates a PDF with incremental builds and checks the correctness of retained pages.
- **Tests for `write_filtered_pdf()`**: Confirms that the final output PDF contains only the expected pages.

### `requirements.txt`

Lists all dependencies required for the project:

```
PyMuPDF==1.22.5
PyPDF2==3.0.1
ReportLab==3.6.12
```

## Design Choices

- **Rule-Based Filtering:** The decision to use a rule-based approach instead of machine learning was made to ensure deterministic behavior and transparency in slide selection.
- **PyMuPDF for Text Extraction:** PyMuPDF (Fitz) was chosen over other libraries like PDFMiner due to its superior accuracy in text and image extraction.
- **GUI Implementation:** A Tkinter-based GUI was implemented to make the tool accessible to non-technical users.
- **Unit Testing:** The project follows a test-driven approach to ensure reliability and maintainability.

## Usage Instructions

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash
   python project.py
   ```

3. Select an input PDF file.
4. Specify the output file name and location.
5. Click **"Process"** to generate the filtered PDF.
6. Check the output directory for the refined PDF.

---

This project is a useful tool for professionals and students who work with slide-based PDFs and need an efficient way to remove redundant slides. With its easy-to-use interface and intelligent filtering capabilities, **SlideSift** offers a practical solution to streamline presentations.
