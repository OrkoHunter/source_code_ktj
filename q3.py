from math import sqrt

try:
    input = raw_input
except:
    pass

def F(n):
    """Return nth fibonacci number"""
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

if __name__ == '__main__':
    no = input()
    result = 0
    try:
        result = (F(int(no)+1))**2
    except:
        pass
    print(int(result))
