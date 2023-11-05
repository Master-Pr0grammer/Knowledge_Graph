from flask import Flask, jsonify, send_from_directory, abort, request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
import os
import main 


app = Flask(__name__)

# Receive requests for any domain ( Temporary Solution )
CORS(app, resources={r"/*": {"origins": "*"}})

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Get a list of all the files 
@app.route('/backend', methods=['GET'])
def list_results():
    results_dir = '.'
    files = [f for f in os.listdir(results_dir) if f.endswith('.json')]
    return jsonify(files)

# Get each individual file 
@app.route('/api/backend/<filename>', methods=['GET'])
def get_result(filename):
    results_dir = '.'
    filepath = os.path.join(results_dir, filename)
    if filename.endswith('.json') and os.path.exists(filepath):
        return send_from_directory(results_dir, filename)
    else:
        abort(404, description="Resource not found")


@app.route('/upload-text-files', methods=['POST'])
def upload_text_files():
    user_inputs_dir = os.path.join(app.root_path, 'user_files')
    
    # Create directory if it does not exist
    if not os.path.isdir(user_inputs_dir):
        os.makedirs(user_inputs_dir, exist_ok=True)

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.txt'):
        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join(user_inputs_dir, filename))
        except Exception as e:
            # log exception
            app.logger.error(f'Error saving file: {e}')
            return jsonify({'error': 'Failed to save file'}), 500
    else:
        return jsonify({'error': 'Invalid file type or empty filename'}), 400

    # Call function
    filepath = "./user_files/" + file.filename 
    
    main.upload(file_path=filepath, json_filename="ouput.json")

    return jsonify({'message': 'File uploaded successfully'}), 200




if __name__ == '__main__':
    app.run(debug=True)


