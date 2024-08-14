from flask import Flask, request, send_from_directory, jsonify
from app.services import Services
from db.mysql_repository import MysqlRepository
import os

app = Flask(__name__)
repo = MysqlRepository()
service = Services(repo)

@app.route('/')
def index():
    return send_from_directory('Web', 'lingclassifier.html')


@app.route('/add_text', methods=['POST'])
def add_text():
    data = request.get_json()
    text = data.get('text')
    text_name = data.get('text_name')
    text_source = data.get('text_source')
    text_lang = data.get('text_lang')
    text_genre = data.get('text_genre')

    if not all([text, text_name, text_source, text_lang, text_genre]):
        return jsonify({'error': 'Missing Data'}), 400

    try:
        text_id = service.add_text(text, text_name, text_source, text_lang, text_genre)
        return jsonify({'text_id': text_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_all_texts', methods=['GET'])
def get_all_texts():
    try:
        texts = service.get_all_texts()
        return jsonify(texts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
