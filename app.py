from flask import Flask
#example demo commit message
#now lets try with invalid commit messages
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask Webhook Demo 🚀"

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
