from flask import Blueprint, request, jsonify
from app.services.classifier import classify_text
import re

classify_bp = Blueprint('classify', __name__)

@classify_bp.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    text = data.get("text", "").strip()


    # Regex para apenas permitir letras, números, espaços e pontuação básica
    ALLOWED_CHARS = re.compile(r"^[\w\s,.!?áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ'-]+$", re.UNICODE)

    if not text:
        return jsonify({"error": "Texto em falta"}), 400

    # Validação do conteúdo do texto (ex: evitar código, scripts ou ruído)
    if len(text) > 280:
        return jsonify({"error": "Texto demasiado longo"}), 400

    if not ALLOWED_CHARS.match(text):
        return jsonify({"error": "Texto contém caracteres não permitidos"}), 400
    

    intent, confidence = classify_text(text)

    return jsonify({
        "intent": intent,
        "confidence_score": round(confidence, 4)
    })
