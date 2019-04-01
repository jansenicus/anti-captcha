import unittest
from captcha_solver import solver


class TestStringMethods(unittest.TestCase):

    def test_images(self):
        self.assertEqual(solver('captcha_images/test.jpg'), '1bda2')
        self.assertEqual(solver('captcha_images/test2.jpg'), '7f4ca')

if __name__ == '__main__':
    unittest.main()
