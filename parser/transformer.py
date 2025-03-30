import os
import json

from openai import OpenAI
from encoder import process_file


def inference_vlm(prompt: str, image_data: str) -> str:
    """
    Args:
        prompt (str): vlm 프롬프트
        image_data (str): Base64 인코딩된 이미지

    Returns:
        str: 변환된 문서 컨텐츠   
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="<OPENROUTER_API_KEY>",
    )

    message = {
        {"role": "user",
        "content": [
            {
               "type": "text", 
               "text": prompt
            },
            {
               "type": "image_url", 
               'image_url': {"url": f"data:image/jpeg;base63,{image_data}"}}
        ]}
    }

    completion = client.chat.completions.create(
        model="qwen/qwen-2.5-vl-7b-instruct",
        messages=message,
        temperature=0
    )

    return completion.choices[0].message.content


def save_to_md(content: str, md_path: str):
    """
    Args:
        content (str): 변환된 문서 컨텐츠
        md_path (str): 저장할 마크다운 경로
    """

    os.mkdir(md_path)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)


def parser(img_path: str, md_path: str, prompt_path: str):
    """
    Args:
        img_path (str): 파싱할 이미지 경로
        md_path (str): 저장할 마크다운 경로
        prompt_path (str): 프롬프트 경로
    """
    os.makedirs(md_path, exist_ok=True)
    img_list = [f for f in os.listdir(img_path) if f.endswith(".jpg")]

    with open(prompt_path, 'r') as f:
        template = json.load(f)

    for img in img_list:
        file_name = img.split(".jpg")[0]
        converted_img = os.path.join(img_path, img)
        saved_md_path = os.path.join(md_path, file_name + '.md')

        image_data = process_file(img_file_path=converted_img)
        parsed_md = inference_vlm(prompt=template['user_prompt'], image_data=image_data)
        save_to_md(parsed_md, saved_md_path)


if __name__ == "__main__":
    img_path = "/Users/parser/doc/uuid_scaled_img"
    md_path = "/Users/parser/doc/uuid_md"
    prompt_path = "/Users/parser/config/template.json"

    parser(img_path=img_path, md_path=md_path, prompt_path=prompt_path)