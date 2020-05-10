import unittest

import bamboozler


class BamboozlerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = bamboozler.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Bamboozler', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
