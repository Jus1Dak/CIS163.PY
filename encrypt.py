import unittest

class Salting:
    def __init__(self, text: str, salt: str):
        self.salt = salt #storing salt
        self.cipher_text = self.salter(text) #setting cipher text to the salter function rather than storing it

    def salter(self, text: str):
        return text + self.salt #returns text with salt added
    
    def __str__(self):
        return self.cipher_text[:len(self.cipher_text) - len(self.salt)] #returns ciphertext decrypted by indexing



class ReverseCipher1:
    def __init__(self, text: str):
        self.cipher_text = self.reverse_text(text) #stores function rather than 
        self.reverse_text(text)

    def reverse_text(self, text: str):
        text_lst = list(text) #creates a list of the string
        reverse_text = [] #creating list to store cipher
        for i in range(len(text_lst)-1, -1, -1): #goes through string list backwards
            reverse_text.append(text_lst[i]) #appeneds each indivdual character inside of the list thats storing cipher
        
        return "".join(reverse_text) #joins each letter together

    def __str__(self):
        return self.reverse_text(self.cipher_text)



class ReverseCipher2:
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError
        self.cipher_text = self.reverse_lst(text)
    
    def reverse_lst(self, text: str):
        words = text.split() #splits text
        reversed_words = [] #initalizing list
        
        for word in words:
            reversed_word = self.reverse_word(word) #uses my own reverse function
            reversed_words.append(reversed_word) # appends the word into lst
        
        return ' '.join(reversed_words) #join lst together

    def reverse_word(self, text: str):
        reversed_word = ''
        for i in text: #loops through the text
            reversed_word = i + reversed_word  #adds char to the string through indexing whilst going through the loop when the words are backwards
        return reversed_word #returns function
    
        
    def __str__(self):
        return self.reverse_lst(self.cipher_text)

if __name__ == "__main__":
    c = ReverseCipher2("Hello, World!")
    print(c)

        
    
class XORCipher:
    def __init__(self, text: str, key: str):
        self.key = key
        self.cipher_text = self.convert(text, key)
        if not isinstance(text, str):
            raise TypeError

    def new_key(self, text: str, key: str):
        lst = []
        key_idx = 0

        for i in range(len(text)):
            if key_idx == len(key):
                key_idx = 0
            lst.append(ord(key[key_idx]) ^ ord(text[i]))
            key_idx += 1
        return lst
        
    def convert(self, text: str, key: str):
        new_lst = self.new_key(text, key)
        encrypt = ""

        for i in range(len(new_lst)):
            encrypt += chr(new_lst[i])
        return encrypt
        
    def __str__(self):
        return self.convert(self.cipher_text, self.key)
    

class CaesarCipher:
    def __init__(self, text: str, key: int):
        self.key = key
        self.cipher_text = self.encrypt(text, key)

    def encrypt(self, text: str, key: int): 
        result = list() #creates a list to store all the characters once converted
        for i in text:
            if i.isupper():
                result.append(chr((ord(i) - 65 + key) % 26 + 65)) #converts character into number then subtracts
                # 65 then adds key to return number and modulos it by 26 to check for if your going over 26 then adds 65 to account for overadding
            elif i.islower():
                result.append(chr((ord(i) - 97 + key) % 26 + 97)) #does same thing except with 97
            else:
                result.append(i) #accounts for special characters
        return "".join(result) #creates the new string
    

    def __str__(self):
        return self.encrypt(self.cipher_text, - self.key)
    

    


class VigenereCipher:
    def __init__(self, text: str, key: str):
        self.key = key
        self.cipher_text = self.encrypt(text)

    def new_key(self, text: str):
        new_key1 = (self.key * (len(text) // len(self.key))) + self.key[:len(text) % len(self.key)]
        return new_key1

    def encrypt(self, text: str):
        result = []
        key1 = self.new_key(text)

        for i in range(len(text)):
            temp = key1[i]
            temp1 = text[i]

            if temp.isupper():
                shift = ord(temp1.upper()) - 65  #shifts the charcters
                char = chr((ord(temp) - 65 + shift) % 26 + 65)
                result.append(char)
            elif temp1.islower():
                shift = ord(temp.lower()) - 97  #shifts the characters
                char = chr((ord(temp) - 97 + shift) % 26 + 97)
                result.append(char)
            else:
                result.append(temp1)  # excpetion for special chars

        return ''.join(result)

    def __str__(self):
        return self.encrypt(self.cipher_text)
    





class CustomMappingCipher:
    def __init__(self, text: str):
        self.character_map = {
        'a': ',', 'b': 'c', 'c': '/', 'd': '&', 'e': 'k', 'f': '}', 'g': '4', 'h': 'w', 
        'i': '>', 'j': 'b', 'k': 'W', 'l': 'P', 'm': 'V', 'n': '$', 'o': '"', 'p': '`', 
        'q': 'U', 'r': 'x', 's': '~', 't': 'o', 'u': 'K', 'v': 'B', 'w': ']', 'x': 'e', 
        'y': '[', 'z': '7', 'A': 'H', 'B': 'i', 'C': 'G', 'D': 's', 'E': ';', 'F': 'A', 
        'G': 'y', 'H': 'g', 'I': 'r', 'J': '%', 'K': 'p', 'L': '^', 'M': 'C', 'N': '6', 
        'O': 'O', 'P': '8', 'Q': '3', 'R': '\\', 'S': '5', 'T': '0', 'U': 'Y', 'V': '1', 
        'W': '+', 'X': '{', 'Y': '2', 'Z': 'D', '0': '(', '1': '=', '2': '?', '3': 'q', 
        '4': '<', '5': 't', '6': 'f', '7': 'L', '8': '|', '9': 'l', '!': 'Q', '"': 'F', 
        '#': 'h', '$': ')', '%': 'X', '&': 'd', "'": 'j', '(': '.', ')': 'v', '*': 'E', 
        '+': "'", ',': '#', '-': '@', '.': '*', '/': 'z', ':': 'S', ';': ':', '<': 'N', 
        '=': 'Z', '>': ' ', '?': 'T', '@': '-', '[': 'R', '\\': 'u', ']': 'M', '^': '9', 
        '_': '_', '`': 'a', '{': 'n', '|': 'I', '}': 'J', '~': '!', ' ': 'm'
        }
        self.cipher_text = self.custom_cipher(text)
        if not isinstance(text, str):
            raise TypeError
    
    def decrypt(self, text: str):
        result = list()
        for i in text:
            for key, value in self.character_map.items():
                if i == value:
                    result.append(key)
        return "".join(result)


    def custom_cipher(self, text: str):
        result = list()
        for i in range(len(text)):
            if text[i] in self.character_map.keys():
                result.append(self.character_map[text[i]])
        
        return "".join(result)


    def __str__(self):
        return self.decrypt(self.cipher_text)
    
