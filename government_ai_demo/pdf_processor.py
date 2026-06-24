import fitz

def extract_text(pdf_path):

    pdf = fitz.open(pdf_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    return text


if __name__ == "__main__":

    text = extract_text("sample.pdf")

    print(text)
