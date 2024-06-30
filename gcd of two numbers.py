def gcd(a,b):
    if (a==0):
        return b
    if (b==0):
        return a
    if (a==b):
        return a
    if (a>b):
        return  gcd(a-b,a)
    return gcd(a,b-a)
a = 69
b = 89
if (gcd(a,b)):
    print("GCD of",a,"and",b,"is",gcd(a,b))
else:
    print("not found")
