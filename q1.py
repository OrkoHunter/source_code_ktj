#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

import itertools
import string

my_dict = {}  # Dict matching 'a' with 0, 'b' with 1, etc.
for number in range(len(string.ascii_lowercase)):
    my_dict[string.ascii_lowercase[number]] = number

def join(str1, str2):
    """Returns new string taking alternate elements from str1 and str2"""
    new = ""
    index = -1
    for i in range(min(len(str1), len(str2))):
        index += 1
        new += str1[i]
        new += str2[i]
    if len(str2) > len(str1):
        new += str2[index+1:]
    else:
        new += str1[index+1:]

    return new


def numberify(text):
    """Replace all the strings to numbers"""
    for key, value in my_dict.items():
        text = text.replace(key, str(my_dict[key]))

    return str(int(text) << 1)


if __name__ == '__main__':
    text_a = '27012017'  # Date of event
    text_b = input()
    accepted_chars = string.ascii_letters + '0123456789'
    to_continue = True
    for char in text_b:
        if char not in accepted_chars:
            to_continue = False

    if len(text_b) < 8:
        to_continue = False

    if to_continue is False:
        print(0)
    else:
        print(join(text_a, numberify(text_b)))
