import sys

def latex_conv(filename):

    latex_file = filename.split('.')[0]+'.tex'

    with open(filename, 'r') as fp:
        with open(latex_file, 'w+') as lp:
            pass

if __name__ == '__main__':
    latex_conv(sys.argv[1])
