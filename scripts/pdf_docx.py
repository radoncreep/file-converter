from pdf2docx import Converter
from docx2pdf import convert


def convert_pdf_to_docx(pdf_file, docx_file):
    # Initialize Converter object
    cv = Converter(pdf_file)

    # Convert the PDF file to DOCX
    cv.convert(docx_file, start=0, end=None)

    # Close the Converter object
    cv.close()


# Example usage:
pdf_file = "input.pdf"
docx_file = "output.docx"
convert_pdf_to_docx(pdf_file, docx_file)


def convert_docx_to_pdf(docx_file, pdf_file):
    # Convert DOCX to PDF
    convert(docx_file, pdf_file)


# Example usage:
docx_file = "input.docx"
pdf_file = "output.pdf"
convert_docx_to_pdf(docx_file, pdf_file)
