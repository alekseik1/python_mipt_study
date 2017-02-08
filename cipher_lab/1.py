import random
from collections import Counter
import itertools

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


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

class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # FIXME

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}  # FIXME

    def freq_an(self, s):
        assert isinstance(s, str)
        cntr = Counter([x for x in s])
        for i in cntr:
            cntr[i] /= len(s)
        return cntr

    def freq_an_without_counter(self, s):
        assert isinstance(s, str)


    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        pass  # FIXME

class Norm_Class:
    dic = {'о':'в', 'р':'г', 'ц':'о', 'м':'д', 'т':'у', 'г':'и', 'е':'ш', 'с':'м', 'ч':'к', 'щ':'е', 'э':'а', 'ю':'н',
           'я':'л', 'х':'ь', 'ы':'й', 'ж':'р', 'п':'ф', 'а':'п', 'н':'ж', 'б':'т', 'з':'ы', 'ш':'с', 'й':'з', 'и':'я', 'в':'х',
           'ф':'ю', 'ь':'б', 'л':'ч', 'ё':'ц', 'д':'ё', 'ъ':'щ', 'к':'э', 'у':'ъ'}

    def change_text(self, text):
        return ''.join([self.dic.get(char.lower(), char.lower()) for char in text])

    def test(self, text):
        alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        s = open('12', 'r').read()
        for i in alpha:
            if i not in s:
                print(i)
        #print(s)

def start_atbash():
    cipher = Atbash()
    line = input()
    while line != '.':
        print(cipher.encode(line))
        line = input()

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

def start_mono():
    key = Monoalphabet.alphabet[:]
    random.shuffle(key)
    cipher = Monoalphabet(key)
    line = input()
    while line:
        print(cipher.encode(line))
        line = input()


def start_norm_class():
    n = Norm_Class()
    print(n.change_text(input()))

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def caesar_reverse(self, letter, shift):
        return self.caesar(letter, -shift)

    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)

        return ''.join(ciphertext)

    def decode(self, line):
        result = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar_reverse(letter, shift)
            result.append(cipherletter)
        return ''.join(result)

def start_kizhner(keyword='виженера'):
    #keyword = input('keyword=')
    cipher = Vigenere(keyword)

    line = input()
    while line != '.':
        #print(line)
        print(cipher.decode(line))
        line = input()

#start_norm_class()

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def brute():
    A = [''.join(x) for x in product(alphabet, repeat=8)]
    print(A)

#start_norm_class()
start_kizhner('столлман')