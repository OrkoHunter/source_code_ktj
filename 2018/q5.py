#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

def padovan(n):
    if (n < 0):
        return 0
    if (n==0 or n==1 or n==2):
        return 1
    return padovan(n-2) + padovan(n-3)

if __name__ == '__main__':
    no = input()
    try:
        no = int(no)
        print (padovan(no+1) * padovan(no-1))
    except Exception as e:
        print(0)