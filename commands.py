import cryptostorm
import configparser


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
    crypto_key = config['cryptography']['key']

    if commands[0] == 'exit':
        initExit()
    elif commands[0] == 'crypt-key':
        if commands[1] == '':
            print(' - ' + crypto_key)
        elif commands[1] == 'new':
            key = cryptostorm.createCryptoKey(alphabet)
            config.set('cryptography', 'key', key)
            config.write(open(conf, 'w'))
            print(' - New key is ' + key)
    elif commands[0] == 'encrypt':
        msg = input('Message: ')
        if commands[3] != '' and commands[2] != '' and commands[1] != '':
            msg = cryptostorm.encryptMsg(msg, commands[3], commands[2], int(commands[1]))
        elif commands[2] != '' and commands[1] != '':
            msg = cryptostorm.encryptMsg(msg, alphabet, commands[2], int(commands[1]))
        elif commands[1] != '':
            msg = cryptostorm.encryptMsg(msg, alphabet, crypto_key, int(commands[1]))
        else:
            msg = cryptostorm.encryptMsg(msg, alphabet, crypto_key)
        if msg is False:
            print(' - Unknown error')
        else:
            print(' - This is encrypted message:\n' + msg)
    elif commands[0] == 'decrypt':
        msg = input('Message: ')
        if commands[3] != '' and commands[2] != '' and commands[1] != '':
            msg = cryptostorm.decryptMsg(msg, commands[3], commands[2], int(commands[1]))
        elif commands[2] != '' and commands[1] != '':
            msg = cryptostorm.decryptMsg(msg, alphabet, commands[2], int(commands[1]))
        elif commands[1] != '':
            msg = cryptostorm.decryptMsg(msg, alphabet, crypto_key, int(commands[1]))
        else:
            msg = cryptostorm.decryptMsg(msg, alphabet, crypto_key)
        if msg is False:
            print(' - Unknown error')
        else:
            print(' - This is decrypted message:\n' + msg)
