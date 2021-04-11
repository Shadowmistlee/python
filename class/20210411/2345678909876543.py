import random
b=0
while True:
    b+=1
    a=random.randint(1,10)
    print(a)
    if a==7:
        print('you got your prize')
        break
    if a==5:
        print('loser')
        break
print('你骰了',b,'次')