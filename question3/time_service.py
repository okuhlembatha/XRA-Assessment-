from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def get_time():
    now = datetime.now()  
    return jsonify({
        "current_date": now.strftime("%Y-%m-%d"),
        "current_time": now.strftime("%H:%M:%S")
    })

if __name__ == "__main__":
    # Run the Flask app on port 8080
    app.run(host="0.0.0.0", port=8080)
