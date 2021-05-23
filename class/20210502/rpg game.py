'''
冒險遊戲
'''
import random as r
print('        -----         --------         -------')#毫無實用功能
print('       |     |        |       |        |      ')
print('       |-----         |       |        |   ---')
print('       | \            |--------        |      |')
print('       |  \           |                --------')
sts = [1, 10, 10, 1000,  0, 0]
def write(sts):
    path = 'ouput.txt'
    f = open(path,'w')
    for i in sts:
        f.write(str(i) + "\n")
    f.close()
def read_file():
    path = 'output.txt'
    f = open(path, 'r')
    text = []
    for line in f:
        text.append(int(line))
    print(text)
    f.close
    return text
def update_life(player_blood):
    get_life = r.randint(1,3)
    new_life = player_blood + get_life
    print('Recovery Life =%d Your blood %d'%(get_life,new_life))
    return new_life
def update_money(money):
    get_money = r.randint(1,10)
    new_money = money + get_money
    print('get money =%d your money %d'%(get_money,new_money))
    return new_money
def fighting(player_blood, money, a,magic_point,magic_attack,monster_blood,mag_or_phy,i,weapon):
    status = [0, 10, 10,1000,0,0,]
    monster_blood = r.randint(2,10)
    print('monster have =%dmonster_blood%d hp')
    d = r.randint(1,10)
    if weapon == 1 :
        player_attack = r.randint(1,10)
    else:
        player_attack = r.randint(1,3)
    while True:
        print('monster attacks!')
        player_blood -= 1
        print('player hp',player_blood)
        mag_or_phy = input('1物理攻擊2魔法攻擊(魔法攻擊具有較高攻擊力)')
        if mag_or_phy == '1':
            print('player',a,'uses physical attack!!!')
            monster_blood -= player_attack
        elif mag_or_phy == '2':
            if magic_point <= 0:
                print('you cannot use magical attack now!!!')
                continue
            else:
                print('player',a,'uses magical attack!!!')
                monster_blood -= magic_attack
                magic_point -=1
                print('monster still have',monster_blood,'hp')
        if monster_blood <= 0:
            print('戰鬥結束，你贏了')
            print('you get ',d,'dollars')
            money += d
            status[0] = 0
            status[1] = player_blood
            status[2] = money
            status[3] = magic_point
            status[4] = magic_attack
            status[5] = monster_blood
            status[6] = mag_or_phy
            return status
        elif player_blood <= 0:
            print('戰鬥結束，你死了')
            print('you lost ',d,' dollars')
            money -= d
            status[0] = 0
            status[1] = player_blood
            status[2] = money
            status[3] = magic_point
            status[4] = magic_attack
            status[5] = monster_blood
            status[6] = mag_or_phy
            return status
        else:
            continue
def boss_fight(player_blood, money, a,magic_point,magic_attack,boss_blood,mag_or_phy,i,weapon):
    status = [0, 0, 0, 0, 0, 0, 0]
    print('monster have =%dboss_blood%d hp')
    d = r.randint(1,10)
    while True:
        print('boss attacks!')
        player_blood -= boss_attack
        print('player hp',player_blood)
        mag_or_phy = input('1物理攻擊2魔法攻擊(魔法攻擊具有較高攻擊力)')
        if weapon == 0 :
            player_attack = r.randint(1,10)
        else:
            player_attack = r.randint(1,3)
            if mag_or_phy == '1':
                print('player',a,'uses physical attack!!!')
                print('       /-/              ')
                print('      / /               ')
                print('     / /       ')
                print('   ====== ')
                print('     /    ')
                boss_blood -=player_attack
            elif mag_or_phy == '2':
                if magic_point <= 0:
                    print('you cannot use magical attack now!!!')
                    continue
                    print('player',a,'uses magical attack!!!')
                else:
                    boss_blood -= magic_attack
                    magic_point -=1
                    print('boss still have',monster_blood,'hp')
            if boss_blood <= 0:
                print('戰鬥結束,你贏了')
                print('you get 50 dollars')
                money += 50
                status[0] = 0
                status[1] = player_blood
                status[2] = money
                status[3] = magic_point
                status[4] = magic_attack
                status[5] = boss_blood
                status[6] = mag_or_phy
                return status
            elif player_blood <= 0:
                print('you lost ',d,' dollars')
                print('戰鬥結束，你死了')
                money -= d
                status[0] = 0
                status[1] = player_blood
                status[2] = money
                status[3] = magic_point
                status[4] = magic_attack
                status[5] = boss_blood
                status[6] = mag_or_phy
                return status
            else:
                continue
'''
main program
'''
event=0
buy = 0
magic_point = 10
mag_or_phy = 0
magic_attack = r.randint(4,8)
monster_blood = r.randint(2,10)
boss_attack = r.randint(3,10)
boss_blood = 50
money = 0
weapon = 0
player_blood =20
player_attack = 0
a= input('enter your name :')
stat = read_file()
while True:
    c = int(input('你想做什麼?(1查看血量2查看錢3隨機事件4買東西5挑戰boss6離開)'))
    if c == 1:
        print(stat[1])
    elif c == 2:
        print(stat[2])
    elif c == 3:
        event=r.randint(1,3)
        if event == 1:
            print('hp recover random')
            stat[1]=update_life(stat[1])
        elif event == 2:
            print('you get random dollar')
            stat[2]=update_money(stat[2])
        elif event == 3:
            print('monster coming!!')
            fighting(player_blood ,money, a,magic_point,magic_attack,monster_blood,mag_or_phy,i,weapon)
            print('player life = %d, money = %d'%(stat[1], stat[2]))
    if c == 4:
        print('what do you want?')
        buy = input('1回復魔法($15)2回復HP($10)3買武器($20)q離開')
        if buy == '1':
            if money <= 14:
                print('you do not have enough money')
                pass
            else:
                print('magic point recover 5')
                money -=15
                pass
        elif buy =='2':
            if money <=10:
                print('you do not have enough money')
                pass
            else:
                print('hp recover 5')
                money -= 10
                pass
        elif buy == 5:
            if money <=10:
                print('you do not have enough money')
                pass
            else:
                money -=20
                weapon =1
                print('trade successful!')
        elif buy == 'q':
            print('你已離開')
            pass
    elif c ==5:
        boss_fight(player_blood,money,a,magic_point,magic_attack,boss_blood,mag_or_phy,i,weapon)
    elif c == 6:
        print('88')
        sts = write(sts)
        break
    else:
        pass