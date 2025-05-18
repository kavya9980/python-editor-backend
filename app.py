from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Python Editor Backend Running"

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get("code")
    stdin = data.get("input", "")

    try:
        result = subprocess.run(
            ['python3', '-c', code],
            input=stdin.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        return jsonify({
            "output": result.stdout.decode('utf-8') + result.stderr.decode('utf-8')
        })
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Error: Code execution timed out."})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})