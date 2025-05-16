import json
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import nltk
from nltk.corpus import stopwords
import os

# Fazer download das stopwords do NLTK (executa uma vez)
nltk.download('stopwords')

# Definir stopwords em português
stop_words_pt = stopwords.words("portuguese")

script_dir = os.path.dirname(os.path.abspath(__file__))  # caminho da pasta onde está o script
dataset_path = os.path.join(script_dir, "intent_dataset.json")  # junta com o nome do ficheiro de treino

model_path = os.path.join(script_dir, 'app', 'models', 'model.pkl') # caminho onde vai ser guardado o modelo já treinado
model_path = os.path.abspath(model_path)

# Carregar o dataset
with open(dataset_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Verifica se colunas existem
if 'text' not in df.columns or 'label' not in df.columns:
    raise ValueError("O dataset deve conter as colunas 'text' e 'label'.")

# Pipeline de NLP
model = Pipeline([
    ('tfidf', TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        stop_words=stop_words_pt
    )),
    ('clf', LogisticRegression(max_iter=1000))
])

# Treinar o modelo
model.fit(df['text'], df['label'])

# Criar pasta se necessário e guardar modelo
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# verifica se o modelo foi guardado corretamente
try:
    joblib.dump(model, model_path)
    print(f"Modelo guardado com sucesso em: {model_path}")
except Exception as e:
    print(f"Erro ao guardar o modelo: {e}")