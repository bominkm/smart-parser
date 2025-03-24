import os

from fitz
from PIL import Image

def resize_image(img_path: str, resized_img_path: str, scale: float = 2):
    """
    Args:
        img_path (str): 원본 이미지 경로
        resized_img_path (str): 변환한 이미지 경로
        scale (float): 배율
    """
    os.makrdirs(resized_img_path, exist_ok = True)
    img_list = [f for f in os.listdir(img_path) if f.endswith(".jpg")]

    for img in img_list:
        image_path = os.path.join(img_path, img)
        resized_image_path = os.path.join(resized_img_path, img)

        with Image.open(image_path) as img:
            new_size = (int(img.width * scale), int(img.height * scale))
            resized_img = img.resize(new_size, Image.LANCZOS)
            resized_img.save(resized_image_path)


def resize_pixmap(pdf_path: str, resized_img_path: str, scale: float = 2):
    """
    Args:
        pdf_path (str): 원본 PDF 경로
        resized_img_path (str): 변환한 이미지 경로
        scale (float): 배율
    """
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pixmap = page.get_pixmap()

        img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        new_size = (int(pixmap.width * scale), int(pixmap.height * scale))
        resized_img = img.resize(new_size, Image.LANCZOS)

        resized_img.save(resized_img_path)