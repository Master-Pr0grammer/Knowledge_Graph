from flask import Flask, jsonify, send_from_directory, abort
from flask_cors import CORS
import os
import json

app = Flask(__name__)
# Enable CORS for only the frontend's domain
CORS(app)

@app.route('/results', methods=['GET'])
def list_results():
    results_dir = '.'
    files = [f for f in os.listdir(results_dir) if f.endswith('.json')]
    return jsonify(files)

@app.route('/api/results/<filename>', methods=['GET'])
def get_result(filename):
    results_dir = '.'
    filepath = os.path.join(results_dir, filename)
    if filename.endswith('.json') and os.path.exists(filepath):
        return send_from_directory(results_dir, filename)
    else:
        abort(404, description="Resource not found")

if __name__ == '__main__':
    app.run(debug=True)


