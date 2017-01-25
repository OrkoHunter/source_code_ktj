#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

def return_sum_of_sqrt(no):
    num = "{0:.2f}".format(round(no**0.5, 2))
    sum = 0
    for digit in num:
        try:
            sum += int(digit)
        except:
            pass

    return sum

if __name__ == '__main__':
    num = input()
    try:
        print(return_sum_of_sqrt(int(num)))
    except:
        print(0)
