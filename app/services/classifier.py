import joblib
import os

# Constrói o caminho absoluto para o ficheiro do modelo treinado (model.pkl)
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, '..', 'models', 'model.pkl')
model_path = os.path.abspath(model_path) 

# Carrega o modelo previamente treinado a partir do ficheiro .pkl
model = joblib.load(model_path)

def classify_text(text):

    try:

        # Aplica o modelo para prever a intenção
        predicted = model.predict([text])[0]            # Prevê a classe (intenção) associada ao texto
        confidence = model.predict_proba([text]).max()  # Obtém a confiança (probabilidade mais alta) da previsão
        return predicted, confidence                    # Devolve a intenção prevista e a confiança
    except Exception as e:
        # Se algo correr mal no processo de previsão, lança erro
        raise RuntimeError(f"Erro na classificação do texto: {e}")