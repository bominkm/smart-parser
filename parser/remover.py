import fitz 

def remove_images(pdf_path: str, removed_pdf_path: str):
    """
    Args:
        pdf_path (str): 원본 PDF 문서 경로
        removed_pdf_path (str): 이미지 제거된 PDF 문서 경로

    Returns:
        None
    """
    doc = fitz.open(pdf_path)
    for page in doc:
        img_list = page.get_images()
        for img in img_list:
            xref = img[0] 
            page.delete_image(xref)

    doc.save(removed_pdf_path)
    doc.close()

if __name__ == "__main__":
    pdf_path = "/Users/parser/doc/uuid.pdf"
    removed_pdf_path = "/Users/parser/doc/uuid_without_img.pdf"

    remove_images(pdf_path, removed_pdf_path)