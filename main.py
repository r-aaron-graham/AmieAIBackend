from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "Amie Chatbot Interface"


@app.get("/generate_token")
def generate_token():
    return {"error": "LiveKit integration is not available in this checkout"}, 503


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)
