# ClassifyAPI Rest

## **Contexto**

**Desafio Técnico | Full-Stack Developer & AI Engineer**
Desenvolver uma **API REST** que receba uma frase de texto do utilizador e a classifique numa das seguintes 6 intenções pré-definidas:

## **Abordagem Técnica da Solução:**

Tal como descrito nos requisitos a solução foi implementada:
-  	Como uma API REST.
-   Endpoint: /classify (método POST).
-   Input (Request Body - JSON): { "text": "frase do utilizador" }
-   Output (Response Body - JSON): { "intent": "intent_classificada", "confidence_score":  0.2688}

**Linguagem/Framework:** Python com Flask »» Devido a trabalhar diariamente em Python e já ter desenvolvido alguns projetos no passado recente em Flask, sinto-me mais confortável ao utilizar Python e Flask.

**Abordagem de Classificação:** 
- Para a tarefa de classificação de intenções, foi utilizado o modelo de Regressão Logística da biblioteca scikit-learn. Optei por esta biblioteca porque já tinha uma noção do seu potencial, visto que fiz uma formação em **Supervised Learning with scikit-learn** (https://www.linkedin.com/in/brunomafigueiredo/details/certifications/) .

Como a LogisticRegression do scikit-learn é uma classe que implementa o algoritmo de Regressão Logística, que é um método estatístico utilizado principalmente para classificação e é útil para prever categorias ou várias classes como neste desafio e tem boa performance em problemas com dados estruturados e vetorizados.
 
 **Estrutura do Projeto:** 

  ClassifyAPI/
  
│
├── app/

│   ├── __init__.py             ← app Flask e junta os módulos

│   ├── routes/

│   │   └── classify.py         ← onde está o endpoint /classify

│   ├── services/

│   │   └── classifier.py       ← onde está a lógica de classificação

│   ├── models/

│   │   └── model.pkl           ← ficheiro do modelo treinado

│

├── tests/

│   └── test_classify.py        ← testes unitários para o endpoint

│

├── intent_dataset.json         ← ficheiro de dados

├── train_model.py              ← script que treina e guarda o modelo

├── requirements.txt            ← configuração do ambiente (instalação de dependências)

└── run.py                      ← ficheiro que corre a app Flask


-   **Rota (`routes/classify.py`)** só trata pedidos e respostas HTTP
    
-   **Serviço (`services/classifier.py`)** faz o trabalho de classificação
    
-   **Modelo (`models/`)** armazena o modelo treinado, assim só se treina se necessário e não se re-treina sempre que a a API é chamada.
 
Optei por esta abordagem porque penso que é mais fácil escalar, alterar o modelo e facilita a manutenção.

## **Pontos Bónus:**
  *Tratamento de Erros:*
	- Texto em falta » Verifica se existe uma frase do utilizador
	- Texto demasiado longo » Verifica se a frase do utilizar tem mais de 280 caráteres (ex: evitar código, scripts, ruído)
	- Texto contém caracteres não permitidos » Verifica se a frase do utilizar tem caracteres não permitidos (ex: evitar código, ataques SQL injection)

## **Configuração do ambiente:**
-   Verificar o conteúdo do ficheiro requirements.txt.

## **Execução da API localmente:**
- Executar train_model.py para inicialmente treinar o modelo
- Executar run.py

## **Execução de testes unitários:**
- Executar test_classify.py

## **Execução de interação com a API utilizando Postman:**





## **Sugestões:**

- Modelo de Classificação »  Poderíamos utilizar modelos mais complexos como Random Forests ou redes neuronais.
- Considerações sobre "Contexto" » Poderíamos identificar um tipo de perfil (B2B - B2C) do utilizador  e assim ajustávamos a classificação, ao saber se o utilizador tem interagido recentemente com temas relacionados com "entregas" ou "devoluções" pode ajudar a desambiguar intenções, se existisse mensagens num chatbot poderíamos utilizar as mensagens anteriores da conversa como contexto adicional.
