from flask import Flask, render_template, request, jsonify
from main import generate_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("prompt")
    if not user_input:
        return jsonify({"error": "Prompt is required."}), 400

    response = generate_code(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
