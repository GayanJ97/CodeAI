import os
import sys
import openai

def generate_code(prompt, api_key):
    """
    Generates code using the OpenAI API.
    """
    if not api_key:
        raise ValueError("Please provide an OpenAI API key.")

    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<your prompt>\"")
    else:
        user_prompt = sys.argv[1]
        # This part of the script will not work without an API key.
        # The GUI is the recommended way to run the assistant.
        print("Please use the GUI to run the assistant.")
