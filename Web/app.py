from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

services = Services()

@app.route("/add_text", methods=["POST"])
def add_text():
    data = request.get_json()
    text = data.get('text')
    text_name = data.get('text_name')
    text_source = data.get('text_source')
    text_lang = data.get('text_lang')
    text_genre = data.get('text_genre')

    if not all([text, text_name, text_source, text_lang, text_genre]):
        return jsonify({"msg": "Missing parameters"}), 400

    text_id = services.add_text(text, text_name, text_source, text_lang, text_genre)
    app.logger.info(f"/add_text - Added text with ID: {text_id}")
    return jsonify({"msg": "success", "text_id": text_id})

@app.route("/get_text/<int:text_id>", methods=["GET"])
def get_text(text_id):
    text = services.get_text(text_id)
    if text:
        return jsonify(text)
    else:
        return jsonify({"msg": "Text not found"}), 404

@app.route("/get_all_texts", methods=["GET"])
def get_all_texts():
    texts = services.get_all_texts()
    return jsonify(texts)

@app.route("/add_words_from_text", methods=["POST"])
def add_words_from_text():
    data = request.get_json()
    text_id = data.get('text_id')
    text = data.get('text')
    lang = data.get('lang')

    if not all([text_id, text, lang]):
        return jsonify({"msg": "Missing parameters"}), 400

    services.add_words_from_text(text_id, text, lang)
    app.logger.info(f"/add_words_from_text - Added words for text ID: {text_id}")
    return jsonify({"msg": "success"})



