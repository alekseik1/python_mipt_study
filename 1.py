import random

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

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        pass  # FIXME

class Norm_Class:
    dic = {'о':'в', 'р':'г', 'ц':'о', 'м':'д', 'т':'у', 'г':'и', 'е':'ш', 'с':'м', 'ч':'к', 'щ':'е', 'э':'а', 'ю':'н'}

    def change_text(self, text):
        return ''.join([self.dic.get(char.lower(), char.lower()) for char in text])

n = Norm_Class()
print(n.change_text(input()))

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

def start_mono():
    key = Monoalphabet.alphabet[:]
    random.shuffle(key)
    cipher = Monoalphabet(key)
    line = input()
    while line:
        print(cipher.encode(line))
        line = input()

#start_caesar()