import os
import sys

def start_message():
    print('LaTEX Research Log')
    
    print('>> 1. Create new file')
    print('>> 2. Edit existing file')
    print('>> 3. Delete file')

def log_edit(filename):
    pass

def main():
    # Test commit
    start_message()

    # HIT CTRL-C TO EXIT
    stat = 0

    while(not stat):
        file_list = os.listdir('./Files')
        stat = input('>>')

        if stat == 1:
            name = input('>> File name:')
            if name not in file_list:
                log_edit(name)
            else:
                cout('LaTEXlogError: File already exists')
        
        elif stat == 2:
            print('>>')
            print('\n'.join(['. '+file for file in file_list]))
            
            name = input('>> File name:')
            if name in file_list:
                log_edit(name)
            else:
                cout('LaTEXlogError: File non-existent')
        
        elif stat == 3:
            name = input('>> File name:')
            
            if name not in file_list:
                s = input('Are you sure you want to delete \''+name+'\'? (y/n)').lower()
                if s == 'y':
                    # Delete file
                    pass
            else:
                cout('LaTEXlogError: File already exists')
            
        else:
            print('LaTEXlogError: Invalid input')

if __name__ == '__main__':
    main()
    