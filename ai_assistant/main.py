import os
import sys
import openai

def generate_code(prompt):
    """
    Generates code using the OpenAI API.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

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
        generated_code = generate_code(user_prompt)
        print("\nGenerated Code:\n")
        print(generated_code)
