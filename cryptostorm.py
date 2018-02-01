from random import randint


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


def checkMsgChars(msg, alphabet):
    alph = list(alphabet)
    msg = list(msg)
    for i in msg:
        if i in alph:
            pass
        else:
            return False
    return True


def checkKey(key, alphabet):
    alph = list(alphabet)
    keys = list(key)
    if len(key) == len(alphabet) and len(keys) == len(alph):
        for i in alph:
            if i in keys:
                pass
            else:
                return False
    else:
        return False
    return True


def encryptMsg(msg, alphabet, key, circle=1):
    if checkMsgChars(msg, alphabet) and checkKey(key, alphabet):
        alph = list(alphabet)
        keys = list(key)
        y = msg
        print(len(alph))
        for z in range(circle):
            encrypted_msg = []
            for i in range(len(y)):
                print(z+1, alph[alph.index(y[i])], keys[alph.index(y[i])])
                encrypted_msg.append(keys[alph.index(y[i])])
            y = ''.join(encrypted_msg)
        return ''.join(encrypted_msg)
    elif not checkMsgChars(msg, alphabet):
        return False
    elif not checkKey(key, alphabet):
        return False
    else:
        return False
