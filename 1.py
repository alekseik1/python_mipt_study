__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-


class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {}
        for i in range(len(self.alphabet)):
            encoded = self.alphabet[i]
            letter = self.alphabet[(i + key) % len(self.alphabet)]
            self._decode[letter] = encoded
            self._decode[letter.upper()] = encoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._encode.get(char, char) for char in line])


def start_atbash():
    cipher = Atbash()
    line = input()
    while line != '.':
        print(cipher.encode(line))
        line = input()

# 19

def start_caesar(key=19):
    #key = int(input('Ээъыцмъ фубз:'))
    cipher = Caesar(key)
    line = input()
    while line != '.':
        #for i in range(33):
        #    cipher = Caesar(i)
        #    print(cipher.decode(line), i)
        print(cipher.decode(line))
        line = input()

start_caesar()