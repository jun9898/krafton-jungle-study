import configparser

config = configparser.ConfigParser()
x = 1
y = x*3
config['system'] = {}
config['system']['setting1'] = str(x)
config['system']['setting2'] = str(y)
print("hello world")


with open('config.ini', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

config.read('config.ini', encoding='utf-8')

config.sections()

ver = config['system']['setting1']
title = config['system']['setting2']

print(title,ver)
# how to use configpaser

