import configparser
from random import randint

config = configparser.ConfigParser()
config.read('conf.ini')
language = config['cryptography']['language']


def createCryptoKey():
    lang = [i for i in language]
    key_parts = []

    for i in range(len(lang)):
        temp = randint(0, len(lang) - 1)
        char = lang[temp]
        key_parts.append(char)
        del lang[lang.index(char)]

    key = ''.join(key_parts)

    return key


print(createCryptoKey())

# def encryptByConfig(self, msg):
