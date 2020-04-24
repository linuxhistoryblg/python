#!/usr/bin/env python3
from subprocess import run
from sys import argv
from sys import exit
''' Demonstrate command line args passed to python when using
    if __name__=="__main__" construction. Call makefile.py <filename>
    at the command line to create an empty file with name <filename>.
'''

def makefile(file):
    run(['touch',file])

if __name__ == "__main__":
    '''touch the file given as the first argument, if given
       if argv < 1, return usage statement. A more sophisticated
       handling of arguments could be implemented with argpase
    '''
    try:
        makefile(argv[1])
    except IndexError:
        print('Usage: makeafile <filename>')
        exit(69)
