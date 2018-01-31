#!/usr/bin/env python
import string
try:
    input = raw_input
except:
    pass

if __name__ == '__main__':
    print ("NIRVANA is the hint")
    nirwana_lower= "NIRVANA".lower()
    no = input()
    try:
        ans = ''
        if (all([i in string.ascii_letters for i in no])):
            no = no.lower()
            num_ind = -1
            for char in no:
                num_ind +=1
                to_add = (string.ascii_letters.index(char) + string.ascii_letters.index(nirwana_lower[num_ind%7]))%26
                ans += string.ascii_letters[to_add]
        print(ans)
    except Exception as e:
        print(0)