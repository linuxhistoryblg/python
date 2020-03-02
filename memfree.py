#!/usr/bin/env python3
# compute free memory
from psutil import virtual_memory as vmem

meg = 1000000
gig = 1000000000

mem = vmem()
total = mem.total
free = mem.free
used = mem.used

if free / gig < 1:
    denom = 'MB_FREE'
    denom_free = free / meg
else:
    denom = 'GB_FREE'
    denom_free = free / gig

def to_percent(total,free):
    '''Return percent of memory in free'''
    return free/total*100
print(f'TOTAL: {total/gig:.2f}GB {denom}: {denom_free:.2f} %FREE: {to_percent(total,free):.0f}%')
