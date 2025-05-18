from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run_code():
    try:
        data = request.get_json()
        code = data.get("code", "")
        user_input = data.get("input", "")

        completed_process = subprocess.run(
            ["python3", "-c", code],
            input=user_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )

        return jsonify({
            "output": completed_process.stdout.decode(),
            "error": completed_process.stderr.decode()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)