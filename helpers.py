import re
from pywin.mfc.docview import Document
from pypdf import PdfReader


def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    reader = PdfReader(file)
    document = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            document.append(text)
    return "".join(document)


def extract_text_from_docx(file) -> str:
    """Extract text from a DOCX file-like using python-docx."""
    document = Document(file)
    parts = []
    for para in document.paragraphs:
        parts.append(para.text)
    return "\n".join(parts)


def extract_text_from_txt(file) -> str:
    """Extract text from a plain text file-like."""
    raw = file.read()
    if isinstance(raw, bytes):
        for enc in ("utf-8", "utf-16", "latin-1"):
            try:
                return raw.decode(enc)
            except:
                continue
        return raw.decode("utf-8", errors="ignore")
    return str(raw)


def extract_text_from_file(uploaded_file):
    """
    Returns (text, name) for a given uploaded file.
    Supported types: pdf, docx, txt, md
    """
    name = uploaded_file.name
    ext = name.lower().split(".")[-1]
    if ext == "pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif ext in ("docx",):
        text = extract_text_from_docx(uploaded_file)
    elif ext in ("txt", "md"):
        text = extract_text_from_txt(uploaded_file)
    else:
        text = extract_text_from_txt(uploaded_file)
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()
