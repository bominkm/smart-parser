import os
import fitz 
from typing import List, Tuple, Dict

def extract_images_from_page(
        page: fitz.Page, doc: fitz.Document
        ) -> List[Tuple[int, Dict[str, str | bytes | int]]]:
    """
    Args:
        page (fitz.Page): PDF 페이지 객체
        doc (fitz.Document): PDF 문서 객체

    Returns:
        List[Tuple[int, Dict[str, str | bytes | int]]]: 
            - List: 추출된 이미지 정보 리스트
            - Tuple[int, Dict]: 각 리스트 요소 (이미지 인덱스, 이미지 정보 딕셔너리)
                - int: 이미지 인덱스
                - Dict[str, str | bytes | int]: 이미지 정보 딕셔너리
                    - "ext" (str): 이미지 확장자 (예: "png", "jpg")
                    - "image" (bytes): 이미지 데이터 (바이너리 형식)
                    - "width" (int): 이미지 가로 크기 (픽셀 단위)
                    - "height" (int): 이미지 세로 크기 (픽셀 단위)
    """
    images = page.get_images(full=True)
    extracted_images = []

    for img_idx, img in enumerate(images):
        xref = img[0] 
        base_image = doc.extract_image(xref)  
        extracted_images.append((img_idx, base_image)) 
    
    return extracted_images


def save_extracted_image(image_data, pdf_img_path, page_num, img_idx):
    """
    Args:
        image_data
        pdf_img_path
        page_num
        img_idx

    Returns:
        None
    """
    image_bytes = image_data["image"]
    ext = image_data["ext"] 

    image_filename = f"page_{page_num + 1}_img_{img_idx + 1}.{ext}"
    image_path = os.path.join(pdf_img_path, image_filename)

    with open(image_path, "wb") as img_file:
        img_file.write(image_bytes)


def extract_images_from_pdf(pdf_path: str, pdf_img_path: str):
    """
    Args:
        pdf_path (str): input pdf file path
        pdf_img_path (str): output image file path

    Returns:
        None
    """

    os.makedirs(pdf_img_path, exist_ok=True)

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = extract_images_from_page(page, doc) 

        for img_idx, image_data in images:
            save_extracted_image(image_data, pdf_img_path, page_num, img_idx) 

    doc.close()


if __name__ == "__main__":
    pdf_path = "/Users/parser/doc/uuid.pdf"
    pdf_img_path = "/Users/parser/doc/uuid_extracted_img"

    extract_images_from_pdf(pdf_path, pdf_img_path)