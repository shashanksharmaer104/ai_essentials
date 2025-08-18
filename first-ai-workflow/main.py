import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_x_post(topic: str) -> str:

    prompt = f"""
    You are an expert social media manager, and you excel at creating viral and highly engaging posts for X (formerly Twitter).

    Your task is to generate a concise and impactful and tailored post based on the user's input. The post should be engaging, relevant, and suitable for a wide audience on X.
    Avoid using hashtags and lot of emojis (few emohies are okay, but not too many). The post should be clear and straightforward, focusing on the message conveyed by the user input.
    
    Keep the post short and structured in a clean, readable way, using the line breaks and empty lines to enhance readability ideally under 280 characters, while ensuring it captures the essence of the user's input.
    
    Here is the user's topic for which you need to generate a post:
    <topic>
    {topic}
    </topic>
    """

    payload = {
        "model": "gpt-4.1-nano",
        "input": prompt
    }

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    response = requests.post(
        "https://api.openai.com/v1/responses",  # Placeholder URL
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"  # Ensure you set your API key in environment variables
        }
    )

    response_txt = response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")

    return response_txt

def main():
    # user input => AI(LLM) to generate X post => output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X Post")
    print(x_post)

if __name__ == "__main__":
    main()
