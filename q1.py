# !/usr/bin/env python

try:
    input = raw_input
except:
    pass

try:
    from functools import reduce
except:
    pass

import operator
import math

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

if __name__ == '__main__':
    try:
        no = int(input())
        w = 1 if (no%2) else -1
        hd = hex(no<<1 + w)
        p = prod([int(x) for x in hd if (x.isdigit() and x!='0')])
        print(p)
    except:
        print(0)
