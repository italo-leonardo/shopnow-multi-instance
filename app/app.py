from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

INSTANCE_ID = os.environ.get("INSTANCE_ID", "unknown")
HOSTNAME = socket.gethostname()

@app.route("/")
def index():
    return jsonify({
        "message": "ShopNow - OK",
        "instance_id": INSTANCE_ID,
        "hostname": HOSTNAME
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Porta interna fixa, o balanceador acessa essa porta
    app.run(host="0.0.0.0", port=5000)
