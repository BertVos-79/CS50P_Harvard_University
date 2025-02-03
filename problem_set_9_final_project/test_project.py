"""
Tests for project.py

We use pytest to test the core functions of SlideSift:
1) parse_page()
2) is_extension()
3) filter_slides_rule_based()
4) write_filtered_pdf()
"""

import subprocess
import sys

# Dictionary of required libraries with versions
required_libraries = {
    "PyMuPDF": "1.22.5",
    "PyPDF2": "3.0.1",
    "reportlab": "3.6.12",
}

def install_missing_libraries():
    """
    Ensures all required dependencies are installed.
    """
    for package, version in required_libraries.items():
        try:
            __import__(package.lower())
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", f"{package}=={version}"]
            )


# Install missing libraries
install_missing_libraries()


# Import installed libraries
import pytest
import fitz  # PyMuPDF
import PyPDF2
from project import (
    SlideInfo,
    FilteredSlides,
    parse_page,
    is_extension,
    filter_slides_rule_based,
    write_filtered_pdf,
)


def test_parse_page():
    """
    Tests parse_page() to verify correct extraction of:
      - first_line (str)
      - remaining_lines (list[str])
      - image_count (int)
    """

    class MockFitzPage:
        def __init__(self, text: str, images: list[tuple] = []):
            self.text = text
            self.images = images

        def get_text(self) -> str:
            return self.text

        def get_images(self, full: bool = True) -> list[tuple]:
            return self.images

    # Create a mock page
    page = MockFitzPage("Hello World\nSecond line", [(1, 2, 3)])
    result = parse_page(page)  # Should return a SlideInfo object

    assert isinstance(result, SlideInfo)
    assert result.first_line == "Hello World"
    assert result.remaining_lines == ["Second line"]
    assert result.image_count == 1


def test_is_extension():
    """
    Tests is_extension() by verifying different cases:
      - Incremental builds should return True
      - Different slides should return False
    """
    # Create SlideInfo objects instead of raw dictionaries
    old_slide = SlideInfo(
        first_line="Model for a linear relation",
        remaining_lines=["something else", "line2"],
        image_count=1,
    )
    new_slide = SlideInfo(
        first_line="Model for a linear relation",
        remaining_lines=["something else", "line2", "new bullet"],
        image_count=1,
    )

    # Should be an extension
    assert is_extension(old_slide, new_slide) is True

    # If new_slide has fewer lines, it is not an extension
    fewer_lines = SlideInfo(
        first_line="Model for a linear relation",
        remaining_lines=["something else"],
        image_count=1,
    )
    assert is_extension(old_slide, fewer_lines) is False

    # Different first line => distinct slide
    diff_first = SlideInfo(
        first_line="This is different",
        remaining_lines=["something else", "line2", "new bullet"],
        image_count=1,
    )
    assert is_extension(old_slide, diff_first) is False

    # Fewer images => not an extension
    fewer_imgs = SlideInfo(
        first_line="Model for a linear relation",
        remaining_lines=["something else", "line2", "new bullet"],
        image_count=0,
    )
    assert is_extension(old_slide, fewer_imgs) is False


def test_filter_slides_rule_based(monkeypatch):
    """
    Tests filter_slides_rule_based() with a mock PDF.
    It simulates slides with incremental builds and checks whether the correct pages are kept.
    """

    class MockFitzPage:
        def __init__(self, text: str, images: list[tuple] = []):
            self.text = text
            self.images = images

        def get_text(self) -> str:
            return self.text

        def get_images(self, full: bool = True) -> list[tuple]:
            return self.images

    class MockFitzDoc:
        def __init__(self, pages: list[MockFitzPage]):
            self._pages = pages

        def __iter__(self):
            return iter(self._pages)

        def __len__(self) -> int:
            return len(self._pages)

        def close(self):
            pass

    def mock_open(path: str):
        pages = [
            MockFitzPage("Slide A"),
            MockFitzPage("Slide A\nnew bullet"),
            MockFitzPage("Slide B", [(123, 456, 789)]),
        ]
        return MockFitzDoc(pages)

    monkeypatch.setattr("fitz.open", mock_open)

    results = filter_slides_rule_based("fake.pdf")

    # Ensure the function returns a FilteredSlides object
    assert isinstance(results, FilteredSlides)

    # Check that correct indices are kept
    assert results.kept_indices == [1, 2]


def test_write_filtered_pdf(tmp_path):
    """
    Tests write_filtered_pdf() by verifying that a new PDF is correctly written with only the kept pages.
    """
    # Create a sample input PDF
    input_pdf_path = tmp_path / "input.pdf"
    output_pdf_path = tmp_path / "output.pdf"

    writer = PyPDF2.PdfWriter()
    for i in range(5):
        writer.add_blank_page(width=612, height=792)  # Standard letter size
    with open(input_pdf_path, "wb") as f:
        writer.write(f)

    # Define which pages to keep
    filtered_slides = FilteredSlides([1, 3])

    # Run function
    write_filtered_pdf(str(input_pdf_path), str(output_pdf_path), filtered_slides)

    # Verify output PDF
    reader = PyPDF2.PdfReader(str(output_pdf_path))
    assert len(reader.pages) == 2  # Should contain only two pages (index 1 and 3)
