import fitz  # PyMuPDF
import os


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


if __name__ == "__main__":
    os.makedirs("data/processed", exist_ok=True)
    sample_pdf = "data/raw_pdfs/sample.pdf"  # Drop your PDF here
    if os.path.exists(sample_pdf):
        content = extract_text(sample_pdf)
        print(content[:1000])  # Preview first 1000 characters
        with open("data/processed/sample.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("Saved processed text.")
    else:
        print("Drop a PDF into data/raw_pdfs/ and rerun.")
