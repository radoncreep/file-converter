import os
from pdfminer.high_level import extract_text


def is_pdf_file(file_path):
    """Check if a file is a PDF based on its extension."""
    return file_path.lower().endswith('.pdf')

def convert_pdf_to_md(pdf_file_path, md_file_path):
    """Convert a PDF file to Markdown."""
    if not is_pdf_file(pdf_file_path):
        print("Error: Input file is not a PDF.")
        return
    
    # Extract text from PDF
    text = extract_text(pdf_file_path)
    
    # Save text as Markdown
    with open(md_file_path, 'w') as f:
        f.write(text)

pdf_file = 'input.pdf'
md_file = 'output.md'

if is_pdf_file(pdf_file):
    convert_pdf_to_md(pdf_file, md_file)
    print("PDF converted to Markdown successfully.")
else:
    print("Error: Input file is not a PDF.")
