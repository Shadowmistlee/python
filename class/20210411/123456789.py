import random as r
a=r.randint(1,999)
b=0
c=1
d=999
while b!=a:
    b=int(input('???'))
    if b>a:
        if d>b:
            d=b
    elif b<a:
        if c<b:
            c=b
    print(c,'到',d)
print('you got it')