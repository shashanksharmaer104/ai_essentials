from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

def generate_x_post(topic: str) -> str:

    prompt = f"""
    You are an expert social media manager, and you excel at creating viral and highly engaging posts for X (formerly Twitter).

    Your task is to generate a concise and impactful and tailored post based on the user's input. The post should be engaging, relevant, and suitable for a wide audience on X.
    Avoid using hashtags and lot of emojis (few emojis are okay, but not too many). The post should be clear and straightforward, focusing on the message conveyed by the user input.
    
    Keep the post short and structured in a clean, readable way, using the line breaks and empty lines to enhance readability ideally, while ensuring it captures the essence of the user's input.
    
    Here is the user's topic for which you need to generate a post:
    <topic>
    {topic}
    </topic>

    Here are some examples of topics and generated posts:
    <examples>
        <example-1>
            <topic>Open LLMs are great because they are more than enough for many workflows and offer free use & 100% privacy!</topic>

            <generated-post>
            Yes, Gemini 2.5 Pro is amazing. But for many tasks, it's too expensive & simply overkill.

            Don't sleep on open LLMs which you can run locally on your MacBook!

            Open LLMs like Gemma 3 can be run locally via Ollama or LM Studio, offer 100% privacy and are more than capable enough for most use-cases and workflows.
            </generated-post>
        </example-1>

        <example-2>
            <topic>Despite LLMs: Learn to code! Because AI-assisted coding > Vibe coding.</topic>

            <generated-post>
            There's never been a better time to learn coding! Seriously!

            Yes, you can vibe code sloppy apps all day.

            If you want to build something that actually works, you need to learn to code though.
            </generated-post>
        </example-2>

        Please use the tone, language, structure , and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
        Don't use the content from the examples!
    """

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=prompt
    )

    return response.output_text

def main():
    # user input => AI(LLM) to generate X post => output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X Post")
    print(x_post)

if __name__ == "__main__":
    main()
