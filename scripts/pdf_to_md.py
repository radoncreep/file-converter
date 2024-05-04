from pdfminer.high_level import extract_text
import markdown2
from weasyprint import HTML


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


def convert_md_to_pdf(md_file_path, pdf_file_path):
    # check file is md_file_path 
    if not md_file_path.lower().endswith('.pdf'):
        print("Error: Input file not md.")
        return 

    # convert md to html for better formatting
    md_file_text = extract_text(md_file_input)

    # html to pdf as output
    convert_html_to_pdf(convert_md_to_html(md_file_text))


def convert_md_to_html(md_file):
    with open(md_file, 'r') as f:
        md_content = f.read()
    html_content = markdown2.markdown(md_content)
    return html_content()


def convert_html_to_pdf(html_file, pdf_file_path):
    HTML(string=html_file).write_pdf(pdf_file_path)


pdf_file = 'input.pdf'
md_file = 'output.md'

md_file_input = 'md_file_input.md'
pdf_file_output = 'pdf_output.md'

if is_pdf_file(pdf_file):
    convert_pdf_to_md(pdf_file, md_file)
    print("PDF converted to Markdown successfully.")
else:
    print("Error: Input file is not a PDF.")
