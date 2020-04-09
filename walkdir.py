import os
from os.path import join, getsize
def walkdir(path):
    for root, dirs, files in os.walk(path):
        try:
            print(root, "consumes", end=" ")
            print(sum([getsize(join(root, name)) for name in files]), end=" ")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
        except FileNotFoundError:
            pass
