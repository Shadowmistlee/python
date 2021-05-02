import random
ans=random.randint(1,999)
b=0
c=999
e=999
d=0
while True:
    a=int(input('???'))
    if a>ans:
        e=a
        print('too big',a,'~',d)
    elif a<ans:
        d=a
        print('too small',a,'~',e)
    elif a==ans:
        print('you got it')
        break
    else:
        print('wtf')