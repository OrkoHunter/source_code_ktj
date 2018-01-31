#!/usr/bin/env python

try:
    input = raw_input
except:
    pass

def largest_palindrome(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)

    return max(results, key=len)

if __name__ == '__main__':
    no = input()
    try:
        if int(no) in [0, 1, 2]:
            print(1)
        else:
            p = largest_palindrome(bin(int(no))[2:])
            print(len(p))
    except Exception as e:
        print(0)
