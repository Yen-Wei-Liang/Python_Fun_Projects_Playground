#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Unit tests for a Caesar cipher program
#===============================================================
import unittest
import Caesar_Cipher
from Caesar_Cipher import Caesar_Cipher

class CaesarCipherTest(unittest.TestCase):

    def test_encrypt(self):

        key_5 = 5
        message_5 = "Cat is so cute"
        expected_result_5 = "Hfy nx xt hzyj"
        result_5 = Caesar_Cipher().encrypt(message_5, key_5)
        self.assertEqual(expected_result_5, result_5)

        key_3 = 3
        message_3 = "Zod is prophet"
        expected_result_3 = "Crg lv surskhw"
        result_3 = Caesar_Cipher().encrypt(message_3, key_3)
        self.assertEqual(expected_result_3, result_3)


        key_1 = 1
        message_1 = "Kddlab is the best"
        expected_result_1 = "Leembc jt uif cftu"
        result_1 = Caesar_Cipher().encrypt(message_1, key_1)
        self.assertEqual(expected_result_1, result_1)


        key_25 = 25
        message_25 = "NCHU EE KDD"
        expected_result_25 = "MBGT DD JCC"
        result_25 = Caesar_Cipher().encrypt(message_25, key_25)
        self.assertEqual(expected_result_25, result_25)

    def test_decrypt(self):

        key_5 = 5
        message_5 = "Hfy nx xt hzyj"
        expected_result_5 = "Cat is so cute"
        result_5 = Caesar_Cipher().decrypt(message_5, key_5)
        self.assertEqual(expected_result_5, result_5)

        key_3 = 3
        message_3 = "Crg lv surskhw"
        expected_result_3 = "Zod is prophet"
        result_3 = Caesar_Cipher().decrypt(message_3, key_3)
        self.assertEqual(expected_result_3, result_3)


        key_1 = 1 
        message_1 = "Leembc jt uif cftu"
        expected_result_1 = "Kddlab is the best"
        result_1 = Caesar_Cipher().decrypt(message_1, key_1)
        self.assertEqual(expected_result_1, result_1)

        key_25 = 25
        message_25 = "MBGT DD JCC"
        expected_result_25 = "NCHU EE KDD"
        result_25 = Caesar_Cipher().decrypt(message_25, key_25)
        self.assertEqual(expected_result_25, result_25)
