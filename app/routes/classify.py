from flask import Blueprint, request, jsonify
from app.services.classifier import classify_text
import re

# Cria um Blueprint para agrupar rotas relacionadas à classificação
classify_bp = Blueprint('classify', __name__)

# Define a rota /classify que aceita apenas o método POST
@classify_bp.route('/classify', methods=['POST'])

def classify():

    # Obtém os dados JSON enviados na requisição
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Erro ao interpretar o JSON"}), 400

    # Extrai o texto do JSON, ou uma string vazia se não existir, e remove espaços em excesso
    text = data.get("text", "").strip()


    # Regex para apenas permitir letras, números, espaços e pontuação básica
    ALLOWED_CHARS = re.compile(r"^[\w\s,.!?áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ'-]+$", re.UNICODE)

    # Validação: o texto não pode estar vazio
    if not text:
        return jsonify({"error": "Texto em falta"}), 400

    # Validação do conteúdo do texto (ex: evitar código, scripts ou ruído)
    if len(text) > 200:
        return jsonify({"error": "Texto demasiado longo"}), 400

    # Validação do conteúdo do texto (ex: evitar código, scripts ou ruído, ataques)
    if not ALLOWED_CHARS.match(text):
        return jsonify({"error": "Texto contém caracteres não permitidos"}), 400
    
    # Classifica o texto, obtendo a intenção e o grau de confiança
    try:
        intent, confidence = classify_text(text)
    except Exception:
        return jsonify({"error": "Erro interno ao classificar o texto"}), 500

    # Retorna a resposta em JSON com a intenção e a confiança arredondada a 4 casas decimais
    return jsonify({
        "intent": intent,
        "confidence_score": round(confidence, 4)
    })