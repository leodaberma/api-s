from flask import Flask, jsonify, request
from pypdf import PdfReader

app = Flask(__name__)

# @app.route('/extract_text', methods=['POST'])
@app.route('/extract_text', methods=['POST'])

def extract_text():
    try:
        # Certifique-se de que um arquivo PDF foi enviado
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        archive = request.files['file']

        # Leia o PDF e extraia o texto
        reader = PdfReader(archive)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(port=5000, host='0.0.0.0', debug=True)
