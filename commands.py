import cryptostorm
import configparser

VERSION = 'v1.0.3'
NAME = 'CryptoStorm Client'
DESCRIPTION = 'CryptoStorm Client for Core v2'


def initExit():
    input('Press Enter to exit...')
    exit()


def getCommands(command):
    commands = command.split(' ')
    [commands.append('') for i in range(3)]
    return commands


def doCommands(commands, conf):
    # Init configuration
    config = configparser.ConfigParser()
    config.read(conf)
    alphabet = config['cryptography']['alphabet']
    key = config['cryptography']['key']

    if commands[0] == 'exit':
        initExit()
    elif commands[0] == 'help':
        print('\'exit\' - close client')
        print('\'check\' - check alphabet and key')
    elif commands[0] == 'ver':
        print(' - ' + NAME)
        print('   ' + DESCRIPTION)
        print('   ' + VERSION)
        print(' - ' + cryptostorm.NAME)
        print('   ' + cryptostorm.VERSION)
    elif commands[0] == 'list':
        if cryptostorm.checkKey(key, alphabet):
            keys = list(key)
            alph = list(alphabet)
            for i in range(len(alph)):
                print(' ' + alph[i] + ' - ' + keys[i])
        else:
            print(' - Key from config does\'t match your alphabet')
    elif commands[0] == 'check':
        if commands[1] == '':
            if cryptostorm.checkKey(key, alphabet):
                print(' - All is normal')
            else:
                print(' - Key from config does\'t match your alphabet')
        elif commands[1] != '' and commands[2] != '':
            if cryptostorm.checkKey(commands[1], commands[2]):
                print(' - Key is normal for this alphabet')
            else:
                print(' - Key does\'t match this alphabet')
        elif commands[1] != '':
            if cryptostorm.checkKey(commands[1], alphabet):
                print(' - Key is normal for your alphabet')
            else:
                print(' - Key does\'t match the your alphabet')
    elif commands[0] == 'key':
        if commands[1] == '':
            print(' - ' + key)
        elif commands[1] == 'new':
            key = cryptostorm.createCryptoKey(alphabet)
            config.set('cryptography', 'key', key)
            config.write(open(conf, 'w'))
            print(' - New key is ' + key)
        elif commands[1] == 'set':
            key = input('Key: ')
            if cryptostorm.checkKey(key, alphabet):
                config.set('cryptography', 'key', key)
                config.write(open(conf, 'w'))
                print(' - Key is ' + key)
            else:
                print(' - Key does\'t match the alphabet')
    elif commands[0] == 'alphabet' or commands[0] == 'alph':
        if commands[1] == '':
            print(' - ' + alphabet)
        elif commands[1] == 'set':
            alph = input('Alphabet: ')
            if cryptostorm.checkAlphabet(alph):
                config.set('cryptography', 'alphabet', alph)
                config.write(open(conf, 'w'))
                print(' - Alphabet is:\n' + alph)
            else:
                print(' - Whitespaces not allowed\n - Use underline')
    elif commands[0] == 'encrypt' or commands[0] == 'ec':
        msg = cryptostorm.convertTo(input('Message: '))

        try:
            if commands[3] != '' and commands[2] != '' and commands[1] != '':
                msg = cryptostorm.encryptMsg(msg, commands[3], commands[2], int(commands[1]))
            elif commands[2] != '' and commands[1] != '':
                msg = cryptostorm.encryptMsg(msg, alphabet, commands[2], int(commands[1]))
            elif commands[1] != '':
                msg = cryptostorm.encryptMsg(msg, alphabet, key, int(commands[1]))
            else:
                msg = cryptostorm.encryptMsg(msg, alphabet, key)
        except cryptostorm.WrongMsg as error:
            print(' - Error: {0}'.format(error))
        except cryptostorm.WrongKey as error:
            print(' - Error: {0}'.format(error))
        except Exception as error:
            print(' - Error: {0}'.format(error))
        else:
            print(' - This is encrypted message: ' + msg[0] + '\n - To decrypt message use this number: ' + str(msg[1]))
    elif commands[0] == 'decrypt' or commands[0] == 'dc':
        while True:
            try:
                start = int(input('Number: '))
                if start < 0:
                    print(' - Error: Start value can\'t be smaller than 0')
                break
            except ValueError:
                print(' - Error: Wrong value')
        msg = cryptostorm.convertTo(input('Message: '))

        try:
            if commands[3] != '' and commands[2] != '' and commands[1] != '':
                msg = cryptostorm.decryptMsg(msg, commands[3], commands[2], start, int(commands[1]))
            elif commands[2] != '' and commands[1] != '':
                msg = cryptostorm.decryptMsg(msg, alphabet, commands[2], start, int(commands[1]))
            elif commands[1] != '':
                msg = cryptostorm.decryptMsg(msg, alphabet, key, start, int(commands[1]))
            else:
                msg = cryptostorm.decryptMsg(msg, alphabet, key, start)
        except cryptostorm.WrongMsg as error:
            print(' - Error: {0}'.format(error))
        except cryptostorm.WrongKey as error:
            print(' - Error: {0}'.format(error))
        except Exception as error:
            print(' - Error: {0}'.format(error))
        else:
            msg = cryptostorm.convertTo(msg, False)
            print(' - This is decrypted message:\n' + msg)
