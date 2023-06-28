def exgcd(a, b):
    print(a, b)
    if a==0:
        return (0, 1 // b)
    
    q = b // a
    r = b % a
    s, t = exgcd(r, a)
    return (t-q*s, s)

print(exgcd(7, 11))