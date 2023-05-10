from configparser import ConfigParser


config = ConfigParser()

ret = config.read('test.ini')


found = False
if ret == []:
    print("INI 파일이 존재하지 않음")
else:
    found = True

# INI 파일이 존재하지 않으면 INI 파일을 생성합니다.
if not found:

    config.add_section('Setting')
    config.set('Setting', 'file_root_config', 'C:/')
    config.set('Setting', 'BTN1', '')
    config.set('Setting', 'BTN2', '')
    config.set('Setting', 'BTN3', '')
    config.set('Setting', 'BTN4', '')
    config.set('Setting', 'BTN5', '')
    config.set('Setting', 'BTN6', '')

    with open('test.ini', 'w') as configfile:
        config.write(configfile)

    print('INI 파일 생성')


else:
   
    file_root_default = config.get('Setting', 'file_root_config')
    btn1 = config.get('Setting', 'BTN1')
    btn2 = config.get('Setting', 'BTN2')
    btn3 = config.get('Setting', 'BTN3')
    btn4 = config.get('Setting', 'BTN4')
    btn5 = config.get('Setting', 'BTN5')
    btn6 = config.get('Setting', 'BTN6')

    config.set('Setting','file_root_config', )

    with open('test.ini', 'w') as configfile:
        config.write(configfile)