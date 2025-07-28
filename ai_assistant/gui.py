import tkinter as tk
from tkinter import scrolledtext
from main import generate_code

class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Chat Assistant")
        self.geometry("400x550")

        self.api_key_label = tk.Label(self, text="OpenAI API Key:")
        self.api_key_label.pack(padx=10, pady=5, anchor='w')

        self.api_key_entry = tk.Entry(self, width=50, show="*")
        self.api_key_entry.pack(padx=10, pady=5, fill=tk.X, expand=False)

        self.chat_history = scrolledtext.ScrolledText(self, state='disabled')
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.prompt_entry = tk.Entry(self, width=50)
        self.prompt_entry.pack(padx=10, pady=5, fill=tk.X, expand=False)

        self.send_button = tk.Button(self, text="Send", command=self.send_prompt)
        self.send_button.pack(padx=10, pady=5)

    def send_prompt(self):
        prompt = self.prompt_entry.get()
        if prompt:
            self.add_to_history(f"You: {prompt}")
            self.prompt_entry.delete(0, tk.END)

            api_key = self.api_key_entry.get()
            if not api_key:
                self.add_to_history("AI: Please enter your OpenAI API key.")
                return

            ai_response = generate_code(prompt, api_key)
            self.add_to_history(f"AI: {ai_response}")

    def add_to_history(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    app = ChatApplication()
    app.mainloop()
