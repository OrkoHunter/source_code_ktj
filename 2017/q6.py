#!/usr/bin/env python

try:
    input = raw_input
except Exception as e:
    pass

import math

def calculate(no):
    # Diff of no and reverse
    d = int(no) - int(''.join(list(reversed(no))))

    # Alternate digits' factorial series
    sum = 0
    to_add = True
    for i in no:
        if to_add:
            sum += math.factorial(int(i))
            to_add = False
        else:
            sum -= math.factorial(int(i))
            to_add = True

    final = sum * d

    return abs(final)

if __name__ == '__main__':
    no = input()
    try:
        t = calculate(no)
        print(t)
    except Exception as e:
        print(0)
        
