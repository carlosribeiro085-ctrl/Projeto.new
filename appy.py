import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Este é meu primeiro deploy no Azure."

if __name__ == "__main__":
    # O Azure define uma variável de ambiente chamada 'PORT'
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
