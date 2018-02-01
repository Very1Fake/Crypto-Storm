import cryptostorm
import configparser


conf = 'conf.ini'
config = configparser.ConfigParser()
config.read(conf)
alphabet = config['cryptography']['alphabet']
crypto_key = config['cryptography']['key']

def initExit():
    input('Press Enter to exit...')
    exit()


def getCommands(command):
    commands = command.split(' ')
    [commands.append('') for i in range(3)]
    return commands


def doCommands(commands):
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
        if commands[1] == '':
            print(' - No message to encrypt')
        else:
            if commands[4] != '' and commands[3] != '' and commands[2] != '':
                msg = cryptostorm.encryptMsg(commands[1], commands[4], commands[3], int(commands[2]))
            elif commands[3] != '' and commands[2] != '':
                msg = cryptostorm.encryptMsg(commands[1], alphabet, commands[3], int(commands[2]))
            elif commands[2] != '':
                msg = cryptostorm.encryptMsg(commands[1], alphabet, crypto_key, int(commands[2]))
            else:
                msg = cryptostorm.encryptMsg(commands[1], alphabet, crypto_key)

            if msg == False:
                print(' - Unknown error')
            else:
                print(' - This is encrypted msg:\n' + msg)

p = '''with open(file, "w") as settings:
    config.write(settings)'''
