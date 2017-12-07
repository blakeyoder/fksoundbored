import unittest

import fksoundbored


class FksoundboredTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fksoundbored.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to FK-Soundbored', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
