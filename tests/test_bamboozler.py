import unittest

from bamboozler.views import API


class BamboozlerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = API.app.test_client()

    def test_index(self) -> None:
        response = self.app.get("/healthz")
        self.assertIn("Service is up and running", response.data.decode())


if __name__ == "__main__":
    unittest.main()
