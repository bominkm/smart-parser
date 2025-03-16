import os
import fitz 

def extract_images_from_page(page, doc):
    """
    Args:
        page: pdf page
        doc: pdf document

    Returns:
        [(img_idx, base_image)]
    """
    images = page.get_images(full=True)
    extracted_images = []

    for img_idx, img in enumerate(images):
        xref = img[0] 
        base_image = doc.extract_image(xref)  
        extracted_images.append((img_idx, base_image)) 
    
    return extracted_images


def save_extracted_image(image_data, pdf_img_path, page_no, img_idx):
    """
    Args:
        image_data
        pdf_img_path
        page_no
        img_idx
    """
    image_bytes = image_data["image"]
    ext = image_data["ext"] 

    image_filename = f"page_{page_no}_img_{img_idx}.{ext}"
    image_path = os.path.join(pdf_img_path, image_filename)

    with open(image_path, "wb") as img_file:
        img_file.write(image_bytes)


def extract_images_from_pdf(pdf_path: str, pdf_img_path: str):
    """
    Args:
        pdf_path (str): input pdf file path
        pdf_img_path (str): output image file path
    """

    os.makedirs(pdf_img_path, exist_ok=True)

    doc = fitz.open(pdf_path)
    for page_no in range(len(doc)):
        page = doc[page_no]
        images = extract_images_from_page(page, doc) 

        for img_idx, image_data in images:
            save_extracted_image(image_data, pdf_img_path, page_no + 1, img_idx + 1) 

    doc.close()


if __name__ == "__main__":
    pdf_path = "/Users/test.pdf"
    pdf_img_path = "/Users/test"

    extract_images_from_pdf(pdf_path, pdf_img_path)