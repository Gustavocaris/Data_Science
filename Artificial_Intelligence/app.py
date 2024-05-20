# Flask é um microframework web em Python que permite construir 
# aplicações web rapidamente

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
#importação dos modulos necessarios para interagir com a API do google

app = Flask(__name__)
# Cria uma instância da aplicação

# --- configuracoes do modelo generativo
GOOGLE_API_KEY = ""  # Substitua pela sua chave API real
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

# --- fim da config do modelo generat

@app.route("/")
def index():
    return render_template("index.html")
#  renderiza o arquivo index.html

# aqui, basicamente, processa as msg do front e inicia outra sessao
@app.route("/send-message", methods=["POST"])
def send_message():
    user_input = request.json["message"]
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    return jsonify({"response": response.text})


# Iniciar o servidor manualmente, caso de algum erro pelo terminal
if __name__ == "__main__":
    app.run(debug=True)



