from random import randint

VERSION = 'v2.0.0rc1'
NAME = 'CryptoStorm Core'


class WrongMsg(Exception):
    pass


class WrongKey(Exception):
    pass


def pickChars(data, mode=True):
    if mode:
        chars = []
        for i in data:
            temp = list(i)
            for i in temp:
                if i not in chars and i != '\n':
                    chars.append(i)
        return chars
    else:
        chars = ''
        for i in data:
            temp = list(i)
            for i in temp:
                if i not in chars and i != '\n':
                    chars += i
        return chars


def createCompletedFile(data):
    file = '\n'.join(data)
    return file


def increaseRotor(rotor, height=256):
    if rotor == height:
        return 0
    else:
        return rotor + 1


def decreaseRotor(rotor, height=256):
    if rotor == 0:
        return height
    else:
        return rotor - 1


def getIndex(lenght, rotor, id, encrypt=True):
    if encrypt is True:
        index = (rotor + id + 1) % lenght
        return index - 1
    else:
        while (id - rotor) < 0:
            id += lenght
        return id - rotor


def createCryptoKey(alphabet):
    alph = list(alphabet)
    key_parts = []

    for i in range(len(alph)):
        temp = randint(0, len(alph) - 1)
        char = alph[temp]
        key_parts.append(char)
        del alph[alph.index(char)]

    key = ''.join(key_parts)

    return key


def convertTo(string, mode=True):
    if mode is True:
        string = string.replace(' ', '_')
    else:
        string = string.replace('_', ' ')
    return string


def checkMsgChars(msg, alphabet):
    alph = list(alphabet)
    msg = list(msg)
    for i in msg:
        if i in alph:
            pass
        else:
            return False
    return True


def checkAlphabet(alphabet):
    alph = list(alphabet)
    for i in alph:
        if i == ' ':
            return False
    return True


def checkKey(key, alphabet):
    alph = list(alphabet)
    keys = list(key)
    if len(key) == len(alphabet) and len(keys) == len(alph):
        for i in alph:
            if i in keys and i != ' ':
                pass
            else:
                return False
    else:
        return False
    return True


def encryptMsg(msg, alphabet, key, height=256):
    if checkMsgChars(msg, alphabet) and checkKey(key, alphabet):
        rotor = randint(0, height)
        alph = list(alphabet)
        keys = list(key)
        y = msg
        encrypted_msg = []
        for i in range(len(y)):
            # print(alph[alph.index(y[i])] + ' -> ' + keys[getIndex(len(alph), rotor, alph.index(y[i] ))] + ' | ' +  str(rotor))
            encrypted_msg.append(keys[getIndex(len(alph), rotor, alph.index(y[i]))])
            rotor = increaseRotor(rotor, height)
        return [''.join(encrypted_msg), rotor - 1]
    elif not checkMsgChars(msg, alphabet):
        raise WrongMsg('Symbols from the message are\'t in the alphabet')
    elif not checkKey(key, alphabet):
        raise WrongKey('Key does\'t match the alphabet')
    else:
        raise


def decryptMsg(msg, alphabet, key, rotor=-1, height=256):
    if checkMsgChars(msg, alphabet) and checkKey(key, alphabet):
        if rotor == -1:
            rotor = randint(0, height)
        alph = list(alphabet)
        keys = list(key)
        y = msg[::-1]
        encrypted_msg = []
        for i in range(len(y)):
            # print(keys[keys.index(y[i])] + ' -> ' + alph[getIndex(len(alph), rotor, alph.index(y[i]), False)] + ' | ' + str(rotor))
            encrypted_msg.append(alph[getIndex(len(alph), rotor, keys.index(y[i]), False)])
            rotor = decreaseRotor(rotor, height)
        result = ''.join(encrypted_msg)
        return result[::-1]
    elif not checkMsgChars(msg, alphabet):
        raise WrongMsg('Symbols from the message are\'t in the alphabet')
    elif not checkKey(key, alphabet):
        raise WrongKey('Key does\'t match the alphabet')
    else:
        raise


def encryptFile(file, alphabet, key, height=256):
    data = open(file, 'r').readlines()
    chars = convertTo(pickChars(data, False))
    if checkMsgChars(chars, alphabet) and checkKey(key, alphabet):
        encrypted_data = []
        rotor = randint(0, height)
        alph = list(alphabet)
        keys = list(key)
        for i in data:
            y = list(convertTo(i))[:-1]
            line = []
            for i in range(len(y)):
                # print(alph[alph.index(y[i])] + ' -> ' + keys[getIndex(len(alph), rotor, alph.index(y[i] ))] + ' | ' +  str(rotor))
                line.append(keys[getIndex(len(alph), rotor, alph.index(y[i]))])
                rotor = increaseRotor(rotor, height)
            encrypted_data.append(''.join(line))
        encrypted_data = createCompletedFile(encrypted_data)
        result = open(file + '.cse', 'w+')
        result.write(encrypted_data)
        result.close()
        return rotor - 1
    elif not checkMsgChars(pickChars(data), alphabet):
        raise WrongMsg('Symbols from the file are\'t in the alphabet')
    elif not checkKey(key, alphabet):
        raise WrongKey('Key does\'t match the alphabet')
    else:
        raise


def decryptFile(file, alphabet, key, rotor=-1, height=256):
    data = open(file, 'r').readlines()
    chars = convertTo(pickChars(data, False))
    if checkMsgChars(chars, alphabet) and checkKey(key, alphabet):
        encrypted_data = []
        if rotor == -1:
            rotor = randint(0, height)
        alph = list(alphabet)
        keys = list(key)
        for i in data:
            y = list(convertTo(i))[:-1]
            line = []
            for i in range(len(y)):
                # print(keys[keys.index(y[i])] + ' -> ' + alph[getIndex(len(alph), rotor, alph.index(y[i]), False)] + ' | ' + str(rotor))
                line.append(alph[getIndex(len(alph), rotor, keys.index(y[i]), False)])
                rotor = decreaseRotor(rotor, height)
            encrypted_data.append(''.join(line))
        encrypted_data = createCompletedFile(encrypted_data)
        result = open(file[:-4], 'w+')
        result.write(encrypted_data)
        result.close()
        return rotor - 1
    elif not checkMsgChars(msg, alphabet):
        raise WrongMsg('Symbols from the message are\'t in the alphabet')
    elif not checkKey(key, alphabet):
        raise WrongKey('Key does\'t match the alphabet')
    else:
        raise
