import os
import fitz

def convert_pdf_to_image(pdf_path: str, img_path: str, img_format: str = "jpg"):
    """
    Args:
        pdf_path (str): 변환할 PDF 경로
        img_path (str): 변환된 이미지 경로
    """
    os.makedirs(img_path, exist_ok=True)

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()

        image_filename = f"page_{page_num + 1}.{img_format}"
        image_path = os.path.join(img_path, image_filename)

        pix.save(image_path)

    doc.close()