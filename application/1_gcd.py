from math import min

def naive_gcd(m, n):
    fm = []
    for i in range(1, m+1):
        if m % i == 0:
            fm.append(i)

    fn = []
    for i in range(1, n+1):
        if n % i == 0:
            fn.append(i)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return cf[-1]


def gcd(m, n):
    i = min(m, n)

    while i > 0:
        if (m % i == 0) and (n % i == 0):
            return i
        else:
            i = i - 1
    
