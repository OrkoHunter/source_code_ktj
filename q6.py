#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

def ktj_in_string(text):
    count = 0
    for char in text:
        if char in ['k', 's', 'h', 'i', 't', 'j']:
            count += 1
    return count

if __name__ == '__main__':
    text = input()
    n = 0
    try:
        n = ktj_in_string(text.lower())
    except Exception as e:
        pass
    print(n)
