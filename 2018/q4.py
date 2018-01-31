#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

if __name__ == '__main__':
    no = input()
    try:
        no = int(no)
        bin_no = bin(no)
        r_bin_no = bin(no >> 1)
        l_bin_no = bin(no << 1)
        num_1 = (bin_no + r_bin_no + l_bin_no).count("1")
        print (num_1)
    except Exception as e:
        print(0)