import joblib
import os

# Carrega o modelo treinado
script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, '..', 'models', 'model.pkl')
model_path = os.path.abspath(model_path)  # resolve '..'

model = joblib.load(model_path)

def classify_text(text):
    # Aqui aplica o modelo para prever a intenção
    predicted = model.predict([text])[0]
    confidence = model.predict_proba([text]).max()
    return predicted, confidence
