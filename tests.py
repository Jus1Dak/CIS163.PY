import unittest
from encrypt import *



class Test_Salting(unittest.TestCase):

    def test_if_works(self):
        self.assertEqual(("GVSU"), Salting("GVSU", "gvsulakers")) #checking if it works properly when encrypted

    def test_encrypted(self):
        self.assertEqual(("GVSUgvsulakers"), Salting.salter("GVSU", "gvsulakers")) #checking if it works properly when dencrypted

    def test_input(self):
        with self.assertRaises(TypeError): #testing for correct inputs
            Salting(str, int)
        with self.assertRaises(TypeError): #testing for correct inputs
            Salting(float, str)
        with self.assertRaises(TypeError): #testing for correct inputs
            Salting(list, str)
        with self.assertRaises(TypeError): #testing for correct inputs
            Salting(dict, str)
    
    def test_no_input(self):
        self.assertEqual((""), Salting("", ""))


class Test_Reverse1(unittest.TestCase):

    def test_if_works(self):
        self.assertEqual("UVSG", ReverseCipher1.reverse_text("GVSU")) #checking if it works properly when encrypted
    
    def test_decrypt(self):
        self.assertEqual("GVSU", ReverseCipher1("GVSU")) #checking if it works properly when dencrypted

    def test_input(self):
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher1(int)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher1(float)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher1(list)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher1(dict)
    

class Test_Reverse2(unittest.TestCase):

    def test_if_works(self):
        self.assertEqual("Hello, World", ReverseCipher2("Hello, World")) #checks for correct output when decrypted

    def test_encrypted(self):
        self.assertRaises("olleH !dlroW", ReverseCipher2.reverse_lst("Hello World!")) #checks for correct output when selfecrypted

    def test_inputs(self):
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher2(int)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher2(float)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher2(float)
        with self.assertRaises(TypeError): #testing for correct inputs
            ReverseCipher2(dict)


class Test_XOR(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual("Hello, Students", self.convert(self.cipher_text, "GVSU"))


    def test_inputs(self):
        with self.assertRaises(TypeError):
            XORcipher()