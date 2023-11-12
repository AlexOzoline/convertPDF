import argparse
from docx2pdf import convert
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Word document to PDF")
    parser.add_argument("input_docx", help="Path to the input Word document")

    args = parser.parse_args()

    input_docx_path = args.input_docx

    # Ensure the provided path is valid
    if not os.path.isfile(input_docx_path):
        print(f"Error: The file '{input_docx_path}' does not exist.")
    else:
        # Convert the Word document to PDF
        convert(input_docx_path)

        print("Conversion successful!")
