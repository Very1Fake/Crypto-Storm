import commands
import configparser

conf = 'conf.ini'
print('crypto-storm v1.0b2')
while True:
    command = input('>> ')

    commands.doCommands(commands.getCommands(command), conf)
