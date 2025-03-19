import base64

def process_file(img_file_path: str) -> str:
    """
    Args:
        img_file_path (str): 이미지 파일 경로

    Returns:
        str: Base64 인코딩된 이미지
    """
    with open(img_file_path, "rb") as f:
        image = f.read()
    image_base64 = base64.b64encode(image).decode("utf-8")
    return image_base64