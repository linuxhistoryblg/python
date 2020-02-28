#!/usr/bin/env python3

from shutil import disk_usage
import sys 

try:
    directory = sys.argv[1]
except IndexError:
    directory = '/'

def main(directory):
    ''' Return disk usage statistics for given directory.'''
    usage = disk_usage(directory)
    total = usage.total / 1000000000
    used = usage.used / 1000000000
    free = usage.free / 1000000000

    def get_percent(total,used):
        used_percent = used/total*100
        return used_percent

    print(f'TOTAL: {total:.2f}GB FREE: {free:.2f}GB USE: {get_percent(total,used):.2f}%')

if __name__ == '__main__':
    main(directory)
