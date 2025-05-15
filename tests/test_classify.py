import unittest
from app import create_app

class TestClassifyEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_classify(self):
        response = self.client.post('/classify', json={'text': 'quero comprar creatina'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('intent', response.json)

if __name__ == "__main__":
    unittest.main()
