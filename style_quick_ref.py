import argparse

from markdown_pdf import MarkdownPdf, Section
from pathlib import Path
# Your custom CSS to control font sizes and borders

parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument("markdown_file")
parser.add_argument("--css", default="quick_ref.css")
parser.add_argument("--output", default=None)

args = parser.parse_args()
output = args.output or args.markdown_file
output = Path(output).with_suffix(".pdf")
css_file: Path = Path(args.css)
markdown_file: Path = Path(args.markdown_file)
with css_file.open("r") as f:
    custom_css: str = f.read()

pdf: MarkdownPdf = MarkdownPdf()

with markdown_file.open("r") as f:
    markdown_content: str = f.read()
    pdf.add_section(section=Section(markdown_content,
                                    paper_size="letter-L", toc=False, borders=(0, 0, 0, 0)), user_css=custom_css)
# Save to a PDF file
pdf.save(file_name=output)
