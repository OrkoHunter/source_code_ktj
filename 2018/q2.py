#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

ANSWER = 42
if __name__ == '__main__':
    no = input()
    try:
        no = int(no)
        if no > 0:
            p = no**2 + ANSWER
        else:
            p = ANSWER - no**2
        print(p)
    except Exception as e:
        print(0)