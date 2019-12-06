import os
import sys
import json

from collections import namedtuple

# Declaring fields of a single record and a named tuple

todo_f  = ['Title', 'isBullets', 'remarks', 'checkList', 'images', 'captions']
Log_r = namedtuple('L_rec', todo_f)


def start_message():
    print('LaTEX Research Log')
    
    print('1. Create new file')
    print('2. Edit existing file')
    print('3. Delete file')

def log_edit(filename):
    fp = open(filename, 'w')
    

def main():

    # HIT CTRL-C TO EXIT (for now)
    stat = 0

    while not stat:
        start_message()
        file_list = os.listdir('./Files')
        stat = int(input('>>> '))

        if stat == 1:
            name = input('>> File name:')
            if name not in file_list:
                log_edit(name)
            else:
                print('LaTEXlogError: File already exists')
        
        elif stat == 2:
            print('>> ')
            print('\n'.join(['. '+file for file in file_list]))
            
            name = input('>>> File name:')
            if name in file_list:
                log_edit(name)
            else:
                print('LaTEXlogError: File non-existent')
                stat = 0
        
        elif stat == 3:
            name = input('>>> File name:')
            
            if name in file_list:
                s = input('Are you sure you want to delete \''+name+'\'? (y/n)').lower()
                if s == 'y':
                    os.remove(name)

            else:
                print('LaTEXlogError: File non-existent')
            
            stat = 0
            
        else:
            print('LaTEXlogError: Invalid input')
            stat = 0

if __name__ == '__main__':
    main()
