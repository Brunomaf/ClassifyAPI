# ClassifyAPI Rest

## **Contexto**

**Desafio Técnico | Full-Stack Developer & AI Engineer**
Desenvolver uma **API REST** que receba uma frase de texto do utilizador e a classifique numa das seguintes 6 intenções pré-definidas:

## **Abordagem Técnica da Solução:**

Tal como descrito nos requisitos a solução foi implementada:
-  	Como uma API REST.
-   Endpoint: /classify (método POST).
-   Input (Request Body - JSON): { "text": "frase do utilizador" }
-   Output (Response Body - JSON): { "intent": "intent_classificada", "confidence_score":  0.2688} - O valor de confiança está entre 0 e 1 (por exemplo, 0.2688), que representa a probabilidade ou grau de confiança da previsão, numa escala decimal.

**Linguagem/Framework:** Python com Flask »» Devido a trabalhar diariamente em Python e já ter desenvolvido alguns projetos em Flask, sinto-me mais confortável ao utilizar Python e Flask.

**Abordagem de Classificação:** 
- Para a tarefa de classificação de intenções, utilizei o modelo de Regressão Logística Multiclasse da biblioteca Scikit-learn. Optei por esta biblioteca por já estar familiarizado com o seu potencial, tendo realizado uma formação em **Supervised Learning with Scikit-learn**.(https://www.linkedin.com/in/brunomafigueiredo).
 
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


-   **Rota (`routes/classify.py`)** só trata pedidos e respostas HTTP (endpoints)
    
-   **Serviço (`services/classifier.py`)** faz o trabalho de classificação
    
-   **Modelo (`models/`)** armazena o modelo treinado, assim só se treina se necessário e não se re-treina sempre que a a API é chamada.
 
Optei por esta abordagem porque penso que é mais fácil escalar, alterar o modelo e facilita a manutenção.

## **Pontos Bónus:**
  *Testes Automatizados:*
  Utilizei os vossos exemplos e através de uma ferramenta de IA criei mais 10 exemplos para cada tipo de intenção. Coloquei esses exemplos num ficheiro - test_cases.json. Desta forma, o ficheiro test_cases.json contém os casos de teste, e cada caso de teste tem pelo menos dois campos: "text": o texto da entrada e "label": a intenção esperada. O teste guarda a intenção correcta (o campo label que está no ficheiro test_cases.json). O teste envia o texto para a API, a API responde, de seguida o teste extrai a intenção prevista da resposta da API e por ultimo, compara com a intenção esperada. O intuito desta abordagem de testes é saber o grau de confiança e os erros (palavras e/ou frases) que são classificadas erradamente pelo modelo.

Segundo os testes realizados e tendo em conta os vossos exemplos - intent_dataset.json - podemos verificar que existe um grau de confiança médio de 23.6%.
Da mesma forma, verificamos que o modelo tem que ser mais robusto, ou temos que classificar melhor a amostra ou temos que aumentar a amostra de exemplos para treinar melhor o modelo, pois dos 60 testes, 21 falharam.

  ![image](https://github.com/user-attachments/assets/2b4f40c0-b71f-4695-906d-e2cadbfca165)

  *Tratamento de Erros:*
  
	- Texto em falta » Verifica se existe uma frase do utilizador
 
	- Texto demasiado longo » Verifica se a frase do utilizar tem mais de 200 caráteres (ex: evitar código, scripts, ruído)
 
	- Texto contém caracteres não permitidos » Verifica se a frase do utilizar tem caracteres não permitidos (ex: evitar código, ataques SQL injection)

*Considerações sobre "Contexto":*
 - Poderíamos identificar um tipo de perfil (B2B - B2C) do utilizador  e assim ajustávamos a classificação;
 - Ao saber se o utilizador tem interagido recentemente com temas relacionados com "entregas" ou "devoluções" pode ajudar a desambiguar intenções;
 - Se existisse mensagens num chatbot poderíamos utilizar as mensagens anteriores da conversa como contexto adicional.

## **Configuração do ambiente:**
-   Verificar o conteúdo do ficheiro requirements.txt.

## **Execução da API localmente:**
- Executar train_model.py para inicialmente treinar o modelo
- Executar run.py

## **Execução de testes unitários:**
- Executar test_classify.py

## **Execução de interação com a API utilizando Postman:**

![image](https://github.com/user-attachments/assets/bf7ed7d7-c664-4133-992e-6bdce72b9858)
![image](https://github.com/user-attachments/assets/53c900e7-59a4-4763-9c78-a00cb250dbc6)
![image](https://github.com/user-attachments/assets/3913c219-c0d6-4c72-832d-9cc35571a0ae)
![image](https://github.com/user-attachments/assets/5e8735bd-94c5-4775-b65c-df1ca6fcd003)
![image](https://github.com/user-attachments/assets/80722d07-8db2-441f-aaad-8384fd67cdb2)


Tratamento de Erros:
**Texto em falta**
![image](https://github.com/user-attachments/assets/8a78d3f7-2a78-41a9-a367-94dbd943eb29)

**Texto demasiado longo**
![image](https://github.com/user-attachments/assets/8188bf64-28c2-48e2-a1ef-b3a88af10316)

**Texto contém caracteres não permitidos**
![image](https://github.com/user-attachments/assets/2646e1d2-25f8-4c83-ae69-53bf83f84031)


## **Sugestões:**

- Usar perfis como features adicionais no modelo, ou seja, utilizar a frase inserida pelo utilizar mais dados do perfil básico (idade, sexo, categoria de compras preferida, frequência de compras, etc);
- Modelo de Classificação »  Poderíamos utilizar modelos mais complexos como Random Forests ou redes neuronais;
- Podiamos criar um "perfil de utilizador" com texto adicional, somando o seu perfil básico às suas interações;
- Armazenar os perfis como vetores por exemplo com embeddings, de forma a ser ágil a utilização dos perfis no treino de modelos.

