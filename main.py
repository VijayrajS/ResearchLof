import os
import sys

def start_message():
    print('LaTEX Research Log')
    
    print('>> 1. Create new file')
    print('>> 2. Edit existing file')
    print('>> 3. Delete file')

def main():
    # Test commit
    start_message()

    # HIT CTRL-C TO EXIT
    stat = 0

    while(not stat):
        file_list = os.listdir('./Files')
        stat = input('>> ')
        if stat == 1:
            name = input('>> File name:')
        elif stat == 2:
            
        elif stat == 3:
            name = input('>> File name:')
            
        else:
            

if __name__ == '__main__':
    main()
    