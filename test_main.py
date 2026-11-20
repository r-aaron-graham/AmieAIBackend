import unittest
from main import app


class LocalBackendTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_landing_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Amie Chatbot Interface", response.data)

    def test_missing_livekit_returns_explicit_error(self):
        response = self.client.get("/generate_token")
        self.assertEqual(response.status_code, 503)
        self.assertIn("LiveKit", response.get_json()["error"])


if __name__ == "__main__":
    unittest.main()
