import random as r
def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(r.randint(1,6))
    return dice
num_dice = int(input('???'))
new_list=roll_dice(6)
print(new_list)
user = roll_dice(num_dice)
print('user result = %s'%user)

comp = roll_dice(num_dice)
print('computer result = %s'%comp)
def who_is_winner(user_list,cmp_list):
    cmp_score=sum(cmp_list)
    usr_score=sum(usr_list)
    print("user score %d"%cmp_score)
    print('computer score%d'%cmp_score)
    if(usr_scroe > cmp_scroe):
        print('user is winner')
    elif(usr_score < cmp_score):
        print('computer is winner')
    else:
        print('draw')
who_is_winner(user_list,cmp_list)