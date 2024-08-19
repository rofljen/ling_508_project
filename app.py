from flask import Flask, request, jsonify, send_from_directory
from services import Services
from db.mysql_repository import MysqlRepository

app = Flask(__name__)
repo = MysqlRepository()
services = Services(repo)

@app.route('/')
def serve_html():
    return send_from_directory('web', 'lingclassifier.html')

@app.route('/add_text', methods=['POST'])
def add_text():
    data = request.json
    text = data.get('text')
    text_name = data.get('text_name')
    text_source = data.get('text_source')
    text_lang = data.get('text_lang')
    text_genre = data.get('text_genre')

    if not all([text, text_name, text_source, text_lang, text_genre]):
        return jsonify({'error': 'All fields are required'}), 400

    try:
        text_id = services.add_text(text, text_name, text_source, text_lang, text_genre)
        return jsonify({'text_id': text_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_all_texts', methods=['GET'])
def get_all_texts():
    try:
        texts = services.get_all_texts()
        return jsonify(texts), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/split_into_sentences', methods=['POST'])
def split_text():
    data = request.json
    text = data.get('text')
    text_lang = data.get('text_lang', 'en')  # Default language is 'en'

    if not text:
        return jsonify({'error': 'Text is required'}), 400

    try:
        sentences = services.split_into_sentences(text, text_lang)
        return jsonify({'sentences': sentences}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
