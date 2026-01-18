import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    if not OpenAI.api_key:
        print("API key not found. Please set OPENAI_API_KEY environment variable.")
        return

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize this Jira ticket in one sentence."}
        ]
    )

    print("AI says:", response.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
