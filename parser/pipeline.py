import os

from extractor import extract_images_from_page, save_extracted_image, extract_images_from_pdf
from remover import remove_images
from convertor import convert_pdf_to_image
from scaler import resize_image
from encoder import process_file
from transformer import inference_vlm

class pdf_parser():
    def __init__(self, pdf_path, local_path, prompt):
        self.pdf_path = pdf_path
        self.local_path = local_path
        self.prompt = prompt

        self.pdf_img_path = os.path.join(local_path, "pdf_images")
        self.removed_pdf_path = os.path.join(local_path, "no_image.pdf")
        self.converted_img_path = os.path.join(local_path, "converted_images")
        self.resized_img_path = os.path.join(local_path, "resized_images")

        self.image_data = None
        self.result = None

    def run(self):
        self.extract_images()
        self.remove_images()
        self.convert_to_images()
        self.resize_images()
        self.encode_images()
        self.infer()
        return self.result

    def extract_images(self):
        extract_images_from_pdf(self.pdf_path, self.pdf_img_path)

    def remove_images(self):
        remove_images(self.pdf_path, self.removed_pdf_path)

    def convert_to_images(self):
        convert_pdf_to_image(self.removed_pdf_path, self.converted_img_path)

    def resize_images(self):
        resize_image(self.converted_img_path, self.resized_img_path)

    def encode_images(self):
        self.image_data = process_file(self.resized_img_path)

    def infer(self):
        self.result = inference_vlm(self.prompt, image_data=self.image_data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python pipeline.py <pdf_path> <local_path> <prompt>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    local_path = sys.argv[2]
    prompt = sys.argv[3]

    pipeline = pdf_parser(pdf_path, local_path, prompt)
    result = pipeline.run()

