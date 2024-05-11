from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

GOOGLE_API_KEY = "AIzaSyCt1mmde7c9Ll_oyYQIs4naQP0MyPBFt38"  # Substitua pela sua chave API real
genai.configure(api_key=GOOGLE_API_KEY)

config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=config,
                              safety_settings=settings)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    user_input = request.json["message"]
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)



