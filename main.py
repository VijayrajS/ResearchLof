import os
import json
from recordtype import recordtype

# TODO:
# * Implement colorama for terminal interface
# * Display note # in prompt
# * Edit note
# * Delete note

# Declaring fields of a single record and a namedtuple
# Note: recordtype is just a mutable version of namedtuple

todo_f = ['ID', 'Title', 'remarks', 'checklist', 'images', 'captions']
L_rec = recordtype('L_rec', ' '.join(todo_f))


def start_message():
    print('\nLaTEX Research Log')

    print('1. Create new file')
    print('2. Edit existing file')
    print('3. Delete file\n')

def print_json(log):
    # ['ID', 'Title', 'remarks', 'checklist', 'images', 'captions']
    print(log)

    print('\nID: ' + str(log.ID))
    # TODO: print the title in bold using colorama
    print(log.Title)

    if log.remarks:
        print(log.remarks)

    if log.checklist:
        print('\n'.join('* ' + u for u in log.checklist))

    if log.images:
        print('Images:')

        for i in range(len(log.images)):
            print(log.images[i] + ' ' + log.captions[i])

    print()

def dict_to_namedtuple(old_dict):
    details = ['','','','','','']

    details[0] = old_dict['ID']
    details[1] = old_dict['Title']

    keys_left = ['remarks', 'checklist', 'images', 'captions']

    for i in range(2,6):
        if keys_left[i-2] in old_dict.keys():
            details[i] = old_dict[keys_left[i-2]]

    return L_rec(*details)

def load_file(fp, mode):
    latest_index = 0
    log_json = []

    fp.seek(0)
    if mode != 1:
        for line in fp.readlines():
            temp_dict = json.loads(line)
            log_json.append(dict_to_namedtuple(temp_dict))

        if log_json:
            latest_index = log_json[-1].ID

    return log_json, latest_index

def new_json(j_index):
    details = [j_index]
    title = input('>>>    Title:')
    remarks = input('>>>    Remarks:')
    check = []
    images = [[],[]]

    if input('>>>    Checklist? y/[n]').lower() == 'y':
        inp = '-'

        print('...    Enter all checklist contents, press a single RETURN key to terminate')

        while inp != '':
            inp = input()
            if inp != '':
                check.append(inp)

    if input('>>>    Images? y/[n]').lower() == 'y':
        img = ['-', '-']

        print('...    Enter image name with caption')

        while img != ['','']:
            img[0] = input()
            img[1] = input()
            print(img)
            if img != ['','']:
                images[0].append(img[0])
                images[1].append(img[1])

    details += [title, remarks, check, images[0], images[1]]

    return L_rec(*details)

def log_edit(filename, mode):

    mode_st = 'w+'
    print('\nOpening ' + './Files/' + filename + '...\n')

    with open('./Files/' + filename, mode_st) as fp:

        close = 0
        log_json, latest_index = load_file(fp, mode)

        print('I     - Insert new note')
        print('V <n> - View note #n')
        print('E <n> - Edit note #n')
        print('C     - Close\n')

        while not close:
            inp = input('./Files/' + filename + '>> ').strip().split()

            if not inp:
                continue

            if inp[0] == 'I':
                log_json += [new_json(latest_index)]
                latest_index += 1

            elif inp[0] == 'V' or inp[0] == 'E':
                if len(inp) != 2:
                    print('LaTEXlogError: wrong number of arguments')
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
                close = 1
                #! Write all JSONs into the file before closing
                fp.writelines([json.dumps(obj._asdict()) for obj in log_json])

            else:
                print('LaTEXlogError: Invalid input')

    fp.close()

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
