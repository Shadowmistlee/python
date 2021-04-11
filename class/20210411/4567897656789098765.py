import random
ans=random.randint(1,100)
print(ans)
b=0
c=100
e=100
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