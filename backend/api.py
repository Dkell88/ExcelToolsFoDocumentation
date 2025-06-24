from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.functions.ExtractIOandConvert import extract_io_list, convert_excel_to_csv

app = Flask(__name__)
CORS(app)

@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json(force=True)
    file_path = data.get('file_path')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    output_file = extract_io_list(file_path)
    if output_file:
        return jsonify({'success': True, 'output_file': output_file})
    return jsonify({'success': False}), 500

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json(force=True)
    file_path = data.get('file_path')
    output_dir = data.get('output_dir')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    result_dir, generated_files = convert_excel_to_csv(file_path, output_dir)
    if result_dir:
        return jsonify({'success': True, 'output_dir': result_dir, 'files': generated_files})
    return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(port=5000)

