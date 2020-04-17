#!/usr/bin/env python3
import subprocess,sys
''' Demonstrate command line args passed to python when using
    if __name__=="__main__" construction. Call makefile.py <filename>
    at the command line to create an empty file with name <filename>.
'''

def makefile(file):
    subprocess.run(['touch',file])

if __name__ == "__main__":
    makefile(sys.argv[1])
