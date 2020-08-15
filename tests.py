import unittest
from smorse import smooshed_morse


class TestSmooshedMorse(unittest.TestCase):
    def test_smooshed_morse(self):
        self.assertEqual(smooshed_morse('sos'), '...---...')
        self.assertEqual(smooshed_morse('daily'), '-...-...-..-.--')
        self.assertEqual(smooshed_morse('programmer'), '.--..-.-----..-..-----..-.')
        self.assertEqual(smooshed_morse('bits'), '-.....-...')
        self.assertEqual(smooshed_morse('three'), '-.....-...')


if __name__ == '__main__':
    unittest.main()
