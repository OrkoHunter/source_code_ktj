#!/usr/bin/env python

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

def cal_ncr(n, r):
    npr = math.factorial(n)/math.factorial(n-r)
    ncr = npr/math.factorial(r)

    return ncr

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

if __name__ == '__main__':
    no = input()
    try:
        n = prod([int(i) for i in no])
        r = sum([int(i) for i in no])
        print(cal_ncr(n ,r))
    except:
        print(0)
