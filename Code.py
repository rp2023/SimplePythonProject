from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/time", methods=["GET"])
def get_time():
    now = datetime.utcnow()
    return jsonify({
        "time": now.strftime("%Y-%m-%d %H:%M:%S UTC")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
