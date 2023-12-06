import base64
import requests
import json

# OpenAI API Key
api_key = "YOUR_OPENAI_API_KEY"

def generate_image_description(image_path):
    # Function to encode the image
    def encode_image(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "generate a brief description of the given image. do not use any symbols or special characters"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 2000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()

    # Extracting the content from the response
    content = response_json['choices'][0]['message']['content']

    return content

# # Example usage:
# image_path = "D:\\GPT\\GPT\\ielts_evaluation\\bar01.png"
# description = generate_image_description(image_path)
# print(description)
