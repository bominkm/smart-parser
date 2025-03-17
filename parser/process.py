import base64
from io import BytesIO
from PIL import Image

def process_file(img_file_path: str, img_format: str = "jpeg") -> str:
    """
    Args:
        img_file_path (str): 이미지 파일 경로
        img_format (str, optional): 이미지 포맷

    Returns:
        str: Base64 인코딩된 이미지
    """
    with Image.open(img_file_path) as image:
        buffered = BytesIO()
        image.save(buffered, format=img_format)
        image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return image_base64