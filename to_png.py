import fitz
file_path = "resume.pdf"
doc = fitz.open(file_path)
for i, page in enumerate(doc):
    pix = page.get_pixmap()
    pix.save(f"resume.png")
    exit()