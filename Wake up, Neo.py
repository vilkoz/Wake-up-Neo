# Copyright (C) 2016 ShRP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author: ShRP
# Email: liberserpentis@gmail.com

from sys import argv, stdout
from time import sleep
from random import uniform
from os import system
from getopt import getopt, GetoptError


def version():

    print('+-------------------------------------------------------------------------------+')
    print('| Wake up, Neo. Copyright (C) 2016 ShRP, Contact: liberserpentis@gmail.com      |')
    print('| Version: 1.0                                                                  |')
    print('|                                                                               |')
    print('| This program comes with ABSOLUTELY NO WARRANTY; for details type `show w`.    |')
    print('| This is free software, and you are welcome to redistribute it                 |')
    print('| under certain conditions; type `show c` for details.                          |')
    print('+-------------------------------------------------------------------------------+')


def usage():

    print('Usage: {0} <options>'.format(argv[0]))

    print('\nOptions:')
    print('  -h: --help                           Print usage and exit')
    print('  -V: --version                        Print version information and exit')
    print('  -A: --available                      Show available colors')
    print('  -C: --color                          [color]: Use this color for Wake up, Neo.')


def available():

    print('+---------------------------------------------------------------------------+')
    print('Available colors:')
    print('+---------------------------------------------------------------------------+')

    print('[~]  (red)')
    print('[~]  (green)')
    print('[~]  (yellow)')
    print('[~]  (blue)')
    print('[~]  (magenta)')
    print('[~]  (cyan)')
    print('[~]  (white)')
    print('[~]  (black)')


def wake_up_neo(color):

    if color == 'red':
        print('\033[1;31m')

    if color == 'green':
        print('\033[1;32m')

    if color == 'yellow':
        print('\033[1;33m')

    if color == 'blue':
        print('\033[1;34m')

    if color == 'magenta':
        print('\033[1;35m')

    if color == 'cyan':
        print('\033[1;36m')

    if color == 'white':
        print('\033[1;37m')

    if color == 'black':
        print('\033[1;30m')

    lines = """Wake up, Neo...
The Matrix has you...
Follow the white rabbit.
Knock, knock, Neo."""

    try:
        for line in lines:
            print(line, end='')

            stdout.flush()
            sleep(uniform(0, 0.6))

            if line == '\n':
                system('clear')

    except (KeyboardInterrupt, SystemExit):
        pass

    finally:
        system('clear')

        print('\033[0;0m')

        exit(1)


def main():

    try:
        opts, args = getopt(argv[1:], 'hVAC:', ['help', 'version', 'available', 'color='])

    except GetoptError: usage()

    else:
        try:
            for opt, arg in opts:
                if opt in ('-h', '--help'): usage(); exit(1)
                if opt in ('-V', '--version'): version(); exit(1)
                if opt in ('-A', '--available'): available(); exit(1)
                if opt in ('-C', '--color'): color = arg

            if color:
                wake_up_neo(color)

        except UnboundLocalError:
            pass

        usage()

if __name__ == '__main__':
        main()
