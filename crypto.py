import commands
import configparser

conf = 'conf.ini'

while True:
    command = input('>> ')

    commands.doCommands(commands.getCommands(command), conf)
