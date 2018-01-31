#!/usr/bin/env python

try:
    input = raw_input
except:
    pass
from math import *

def modify(n):
    n = abs(n)
    sqrt_n = sqrt(n)
    sqrt_n += 1
    log_sqrt_n = 10 * log(sqrt_n, 1024)
    return log_sqrt_n

if __name__ == '__main__':
    no = input()
    try:
        no = int(no)
        print (int(modify(no)))
    except Exception as e:
        print(0)