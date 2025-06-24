from flask import Flask, request, jsonify
from flask_cors import CORS
from excelFunctions.ExtractIOandConvert import (
    extract_io_list_by_rack as extract_io_list_by_rack,
    convert_excel_to_csv as convert_excel_to_csv,
)
from excelFunctions.ExtractKeywords import (
    extract_io_sheets_case_insensitive as extract_io_sheets_case_insensitive,
)
from ioToolset.ioToolset import extract_io_to_xml_imports as extract_io_to_xml_imports
# from ExtractIOandConvert import extract_io_list_by_rack, convert_excel_to_csv
# from ExtractKeywords import extract_io_sheets_case_insensitive
# from ioToolset import extract_io_to_xml_imports


app = Flask(__name__)
CORS(app)

@app.route('/extract_io_list_by_rack', methods=['POST'])
def extract_io_list_by_rack():
    data = request.get_json(force=True)
    file_path = data.get('file_path')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    output_file = extract_io_list_by_rack(file_path)
    if output_file:
        return jsonify({'success': True, 'output_file': output_file})
    return jsonify({'success': False}), 500

@app.route('/convert_excel_to_csv', methods=['POST'])
def convert_excel_to_csv():
    data = request.get_json(force=True)
    file_path = data.get('file_path')
    output_dir = data.get('output_dir')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    result_dir, generated_files = convert_excel_to_csv(file_path, output_dir)
    if result_dir:
        return jsonify({'success': True, 'output_dir': result_dir, 'files': generated_files})
    return jsonify({'success': False}), 500


@app.route('/extract_io_to_xml_imports', methods=['POST'])
def extract_io_to_xml_imports():
    data = request.get_json(force=True)
    file_path = data.get('file_path')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    result_dir, generated_files = extract_io_to_xml_imports(file_path)
    if result_dir:
        return jsonify({'success': True, 'output_dir': result_dir, 'files': generated_files})
    return jsonify({'success': False}), 500

@app.route('/extract_io_sheets_case_insensitive', methods=['POST'])
def extract_io_sheets_case_insensitive():
    data = request.get_json(force=True)
    keywords = data.get('keywords')
    file_path = data.get('file_path')
    output_dir = data.get('output_dir')
    if not file_path:
        return jsonify({'error': 'file_path is required'}), 400

    result_dir, generated_files = extract_io_sheets_case_insensitive(keywords, file_path, output_dir)
    if result_dir:
        return jsonify({'success': True, 'output_dir': result_dir, 'files': generated_files})
    return jsonify({'success': False}), 500


if __name__ == '__main__':
    app.run(port=5000)
