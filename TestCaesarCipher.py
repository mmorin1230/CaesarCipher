import unittest
from CaesarCipher import CaesarCipher  # change to your filename (without .py)

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_word(self):
        cipher = CaesarCipher()
        result = cipher.encrypt("HELLO", 3)
        self.assertEqual(result, "KHOOR")

    def test_encrypt_wraps_around(self):
        cipher = CaesarCipher()
        result = cipher.encrypt("XYZ", 3)
        self.assertEqual(result, "ABC")
    
    def test_decrypt_word(self):
        cipher = CaesarCipher()
        result = cipher.decrypt("KHOOR", 3)
        self.assertEqual(result, "HELLO")
    
    def test_decrypt_wraps_around(self):
        cipher = CaesarCipher()
        result = cipher.decrypt("ABC", 3)
        self.assertEqual(result, "XYZ")

if __name__ == "__main__":
    unittest.main()
