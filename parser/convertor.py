import os
from openai import OpenAI

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
        messages=message
    )

    return completion.choices[0].message.content


def save_to_md(content: str, md_path: str):
    """
    Args:
        content (str): 변환된 문서 컨텐츠
        md_path (str): 마크다운 경로
    """

    os.mkdir(md_path)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
