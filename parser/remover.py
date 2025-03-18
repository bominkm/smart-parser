import fitz 

def remove_images(pdf_path: str, removed_pdf_path: str):
    """
    Args:
        pdf_path (str): 원본 PDF 문서 경로
        removed_pdf_path (str): 이미지 제거된 PDF 문서 경로
    """
    doc = fitz.open(pdf_path)
    for page in doc:
        img_list = page.get_images()
        for img in img_list:
            page.delete_image(img[0])

    doc.save(removed_pdf_path)