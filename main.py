import os
import sys
import json

# TODO:
# * Implement colorama for terminal interface

from collections import namedtuple, defaultdict

# Declaring fields of a single record and a named tuple

todo_f  = ['ID', 'Title', 'remarks', 'checklist', 'images', 'captions']

Log_r = namedtuple('L_rec', todo_f)


def start_message():
    print('\nLaTEX Research Log')
    
    print('1. Create new file')
    print('2. Edit existing file')
    print('3. Delete file\n')

def print_json(log):
    # ['ID', 'Title', 'remarks', 'checklist', 'images', 'captions']
    print(log)
    log = defaultdict(int, log)
    
    print('\nID: ' + str(log['ID']))
    # TODO: print the title in bold using colorama
    print(log['Title'])
    
    if log['remarks']:
        print(log['remarks'])
    
    if log['checklist']:
        print('\n'.join('* ' + u for u in log['checklist']))
    
    if log['images']:
        print('Images:')
        
        for i in range(len(log['images'])):
            print(log['images'][i] + ' ' + log['captions'][i])
    
    print()
    
def log_edit(filename, mode):
    
    mode_st = 'w+' if mode == 1 else 'a+'
    fp = open('./Files/' + filename, mode_st)
    
    print('\nOpening ' + './Files/' + filename + '...\n')
    latest_index = 0
    log_json = []
    
    fp.seek(0)
    if mode != 1:
        for line in fp.readlines():
            log_json.append(json.loads(line))
        
        if log_json:
            latest_index = log_json[-1]['ID']
    
    close = 0
    print('I     - Insert new note')
    print('V <n> - View note #n')
    print('E <n> - Edit note #n')
    print('C     - Close\n')
    
    while not close:
        inp = input('./Files/' + filename + '>> ').strip().split()
        
        if not inp:
            continue

        # ! Take care of insert
        if inp[0] == 'I':
            pass
        
        elif inp[0] == 'V' or inp[0] == 'E':
            if len(inp) != 2:
                print('LaTEXlogError: insufficient args')
                continue
            
            try:
                ind = int(inp[1])
            except:
                print('LaTEXlogError: second argument is an integer')
                continue
            
            if ind >= len(log_json):
                print('LaTEXlogError: index out of bounds')
                continue
            
            print_json(log_json[ind])
            
            if inp[0] == 'E':
                # ? How to edit
                pass
            
        elif inp[0] == 'C':
            print('Closing ' + filename + '...\n')
            fp.close()
            close = 1
        
        else:
            print('LaTEXlogError: Invalid input')

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
                log_edit(name, stat)
            else:
                print('LaTEXlogError: File already exists')
        
        elif stat == 2:
            print('>> ')
            print('\n'.join(['. '+file for file in file_list]))
            
            name = input('>>> File name:')
            if name in file_list:
                log_edit(name, stat)
            else:
                print('LaTEXlogError: File non-existent')
                stat = 0
        
        elif stat == 3:
            name = input('>>> File name:')
            
            if name in file_list:
                del_s = 'Are you sure you want to delete \''
                s = input(del_s + name + '\'? (y/n)').lower().strip()
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
