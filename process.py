import os
import fitz

def extract_img_from_pdf(pdf_path: str, pdf_img_path: str):
    """
    Args:
        pdf_path (str): 대상 pdf 경로
        pdf_img_path (str): 추출된 이미지 저장 경로
    """
    os.makedirs(pdf_img_path, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    
    image_count = 0  
    
    for page_number in range(len(doc)):
        page = doc[page_number]
        images = page.get_images(full=True)  

        for img_idx, img in enumerate(images):
            xref = img[0]  
            base_image = doc.extract_image(xref) 
            img_bytes = base_image["image"]  
            img_ext = base_image["ext"]  

            img_file_name = f"page_{page_number+1}_img_{img_idx+1}.{img_ext}"
            img_path = os.path.join(pdf_img_path, img_file_name)
            
            with open(img_path, "wb") as img_file:
                img_file.write(img_bytes)

            image_count += 1
