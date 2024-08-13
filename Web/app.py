import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from services import Services

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

service = Services()

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return send_from_directory('Web', 'lingclassifier.html')

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

    text_id = service.add_text(text, text_name, text_source, text_lang, text_genre)
    app.logger.info(f"/add_text - Added text with ID: {text_id}")
    return jsonify({"msg": "success", "text_id": text_id})


@app.route('/get_text/<int:text_id>', methods=['GET'])
def get_text(text_id):
    app.logger.info(f"Requested text_id: {text_id}")
    text = service.get_text(text_id)
    if text:
        return jsonify(text.to_dict())
    else:
        return jsonify({"msg": "Text not found"}), 404


@app.route("/get_all_texts", methods=["GET"])
def get_all_texts():
    texts = service.get_all_texts()
    return jsonify(texts)


@app.route("/split_into_sentences", methods=["POST"])
def split_into_sentences():
    data = request.get_json()
    text = data.get('text')
    text_lang = data.get('text_lang')

    if not all([text, text_lang]):
        return jsonify({"msg": "Missing parameters"}), 400

    sentences = service.split_into_sentences(text, text_lang)
    return jsonify({"sentences": sentences})


@app.route("/add_words_from_text", methods=["POST"])
def add_words_from_text():
    data = request.get_json()
    text_id = data.get('text_id')
    text = data.get('text')
    lang = data.get('lang')

    if not all([text_id, text, lang]):
        return jsonify({"msg": "Missing parameters"}), 400

    service.add_words_from_text(text_id, text, lang)
    app.logger.info(f"/add_words_from_text - Added words for text ID: {text_id}")
    return jsonify({"msg": "success"})

if __name__ == "__main__":
    app.run(host='0.0.0.0 ', port=8000, debug=True)