#!/usr/bin/python3
# -*- coding: utf-8 -*-

#standard library
import sys
import os
from time import sleep


def logo():
    #print logo for 2 seconds
    print('\n\n        00010000    10001100        ')
    print('    011101010010    011011001010    ')
    print('  110000100110000  110000000001000  ')
    print('  000110100100000  100011101110001  ')
    print('  011000010101111  100101010011101  ')
    print('   10001111100011  11101000100111   ')
    print('           100010  0010             ')
    print('              001   00              ')
    print('  01         1101  0010         11  ')
    print(' 000110001110010    110101110010111 ')
    print('100101000010110       0100011001001 ')
    print('10000111110101        0111001010001 ')
    print('  010011101100110  0011100010110    ')
    print('    1100110111011  000010000110     ')
    print('       0110100011  01100101111      ')
    print('         10111 10  10 11101         ')
    print('          0010  1  1  1101          ')
    print('            10        10        \n\n')
    print('              Gh0stc0d3         \n\n')
    sleep(2)


def datos():
    #ask for user data and confirm
    print ('\n\tYou must activate "allow less secure apps" in your Gmail account\n')
    mail = input('\nenter your Gmail: ')
    clave = input('type your password: ')
    cam = input('do you want to take pics with your Web Cam? y= yes n = no ')
    id = input('type your computer ID: ')
    os.system('clear')
    print('\n\tMail = {0}, Pass = {1}, Pics = {2}, Computer Id = {3}\n'.format(str(mail), str(clave), str(cam), str(id)))
    chequeo = input('its correct? type "y" or "n" ')
    if chequeo == 'y':
        return mail, clave, cam, id
    else:
        datos()


def generate(mail, clave, template, id):
    #generate output file
    template = open(template, 'r')
    p = template.read()
    file = str(p)
    file += '\nmail = ' + "'" + mail + "'" + '\n'
    file += 'key = ' + "'" + clave + "'" + '\n'
    file += 'id = ' + "'" + id + "'" + '\n'
    file += 'while True:\n'
    file += '\tip = get_ip()\n'
    file += '\tdir2 = screenshot()\n'
    file += '\tsend_mail(mail, key, id, ip, dir2)\n'
    file += '\tip = ""\n'
    file += '\tsleep(300)\n'
    with open('output/thief_finder.py', 'w') as f:
        f.write(file)
        f.close()
    template.close()


sin = 'templates/sin_cam.py'
con = 'templates/con_cam.py'
logo()
mail, clave, cam, id= datos()
if cam == 'y':
    generate(mail, clave, con, id)
else:
    generate(mail, clave, sin, id)

if sys.platform.startswith("win"):
    pyinstaller = input('would you like to make your exe with Pyinstaller? y= yes n = no: ')
    if pyinstaller == 'y':
        os.system('pyinstaller --onefile --noconsole ./output/thief_finder.py')
        print('\n\tYou will find your exe file in "dist" directory ready for Pyinstaller\n')
    else:
        pass
else:
    print('\n\tYou will find your Python file in "output" directory ready for Pyinstaller\n')
    sys.exit(0)

