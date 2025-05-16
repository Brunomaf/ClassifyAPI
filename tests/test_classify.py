import unittest
import os
import sys
import json

# Adiciona o diretório pai ao caminho de importações, permitindo importar o módulo 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a função que cria a aplicação (presumivelmente uma app Flask)
from app import create_app

class TestClassifierBatch(unittest.TestCase):

    # Método que é executado antes de cada teste
    def setUp(self):
        self.app = create_app()                 # Cria uma instância da aplicação
        self.client = self.app.test_client()    # Cria um cliente de teste para fazer chamadas à API

        # Define o caminho para o ficheiro com os casos de teste
        test_file = os.path.join(os.path.dirname(__file__), 'test_cases.json')

        # Carrega os casos de teste a partir do ficheiro JSON
        with open(test_file, encoding="utf-8") as f:
            self.test_cases = json.load(f)

    # Teste principal – envia textos para a API e avalia a intenção e a confiança
    def test_classify_from_file_and_score(self):
        total_confidence = 0                    # Acumulador para a confiança total
        total_tests = len(self.test_cases)      # Número total de testes
        errors = []                             # Lista para guardar os casos que falharam

        for case in self.test_cases:

            # Envia uma requisição POST à rota /classify com o texto do caso de teste
            response = self.client.post('/classify', json={'text': case["text"]})
            self.assertEqual(response.status_code, 200, msg=f"Erro HTTP: {case['text']}")
            
            response_json = response.get_json()
            predicted = response_json.get("intent")                 # Intenção prevista
            confidence = response_json.get("confidence_score", 0)   # Grau de confiança da previsão

            total_confidence += confidence

            expected = case["label"] # Intenção esperada (correcta)

            if predicted != expected:

                # Se a previsão estiver errada, guarda o erro
                errors.append({
                    "text": case["text"],
                    "expected": expected,
                    "predicted": predicted,
                    "confidence": confidence
                })

        average_confidence = total_confidence / total_tests
        print(f"\nMédia de confiança: {average_confidence:.4f}")
        print(f"Número de erros: {len(errors)} de {total_tests} exemplos")

        # Se houve erros, imprime os detalhes
        if errors:
            print("\nErros:")
            for err in errors:
                print(f"→ Texto: {err['text']} | Esperado: {err['expected']} | Previsto: {err['predicted']} | Confiança: {err['confidence']:.2f}")

        # Se mais de 10% dos testes falharem, imprime uma mensagem de falha
        if len(errors) >= total_tests * 0.1:
            print(f"\nFAIL: test_classify_from_file_and_score\n»» Mais de 10% dos testes falharam ({len(errors)} de {total_tests})")
            

if __name__ == "__main__":
    unittest.main()
