import cryptostorm
import configparser
import commands


config = configparser.ConfigParser()
config.read('conf.ini')
alphabet = config['cryptography']['alphabet']


while True:
    command = input('>> ')

    commands.doCommands(commands.getCommands(command))
