from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
import pdfkit


def pdf_to_html(pdf_file_path, html_file_path):
    # Extract text from PDF
    text = extract_text(pdf_file_path)

    # Generate HTML
    soup = BeautifulSoup('<html><body></body></html>', 'html.parser')
    body = soup.body
    body.append(text)

    # Save HTML to file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(str(soup))


def html_to_pdf(html_file_path, pdf_file_path):
    # pdfkit.from_url("https://google.com", "google.pdf", verbose=True)
    pdfkit.from_file(html_file_path, pdf_file_path, verbose=True)


# Example usage
if __name__ == '__main__':
    pdf_file_path_for_pdf_to_html = 'example.pdf'
    html_file_path_for_pdf_to_html = 'output.html'
    pdf_file_path_for_html_to_pdf = 'output.pdf'
    html_file_path_for_html_to_pdf = 'output.html'
    pdf_to_html(pdf_file_path_for_pdf_to_html, html_file_path_for_pdf_to_html)
    html_to_pdf(html_file_path_for_html_to_pdf, pdf_file_path_for_html_to_pdf)
