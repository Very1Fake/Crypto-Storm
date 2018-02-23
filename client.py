import commands
import cryptostorm

conf = 'conf.ini'
print(commands.NAME + ' ' + commands.VERSION)
print(cryptostorm.NAME + ' ' + cryptostorm.VERSION)
while True:
    command = input('>> ')

    commands.doCommands(commands.getCommands(command), conf)
