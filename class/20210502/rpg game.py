'''
冒險遊戲
'''
import random as r
buy = 0
magic_point = 10
mag_or_phy = 0
magic_attack = r.randint(4,8)
monster_blood = r.randint(2,10)
boss_attack = r.randint(3,10)
boss_blood = 50
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
def fighting(player_blood, money, a,magic_point,magic_attack,monster_blood,mag_or_phy):
    status = [0, 0, 0]
    monster_blood = r.randint(2,10)
    print('monster have =%dmonster_blood%d hp')
    d = r.randint(1,10)
    while True:
        print('monster attacks!')
        player_blood -= 1
        print('player hp',player_blood)
        mag_or_phy = int(input('1物理攻擊2魔法攻擊(魔法攻擊具有較高攻擊力)')
        if mag_or_phy == 1:
            print('player',a,'uses physical attack!!!')
            monster_blood -=player_attack
        elif mag_or_phy == 2:
            if magic_point <= 0:
                print('you cannot use magical attack now!!!')
                continue
            else:
                print('player',a,'uses magical attack!!!')
                monster_blood -= magic_attack
                magic_point -=1
                print('monster still have',monster_blood,'hp')
        if monster_blood <= 0:
            print('戰鬥結束,你贏了')
            print('you get ',d,'dollars')
            money += d
            status[0] = 1
            status[1] = player_blood
            status[2] = money
            return status
        elif player_blood <= 0:
            print('戰鬥結束，你死了')
            print('you lost ',d,' dollars')
            money -= d
            status[0] = 0
            status[1] = player_blood
            status[2] = money
            return status
        else:
            continue
def boss_fight(player_blood, money, a,magic_point,magic_attack,boss_blood,mag_or_phy):
    status = [0, 0, 0]
    print('monster have =%dboss_blood%d hp')
    d = r.randint(1,10)
    while True:
        print('boss attacks!')
        player_blood -= boss_attack
        print('player hp',player_blood)
        mag_or_phy = int(input('1物理攻擊2魔法攻擊(魔法攻擊具有較高攻擊力)')
        if mag_or_phy == 1:
            print('player',a,'uses physical attack!!!')
            boss_blood -=player_attack
        elif mag_or_phy == 2:
            if magic_point <= 0:
                print('you cannot use magical attack now!!!')
                continue
            else:
                print('player',a,'uses magical attack!!!')
                boss_blood -= magic_attack
                magic_point -=1
                print('boss still have',monster_blood,'hp')
        if boss_blood <= 0:
            print('戰鬥結束,你贏了')
            print('you get 50 dollars')
            money += 50
            status[0] = 1
            status[1] = player_blood
            status[2] = money
            return status
        elif player_blood <= 0:
            print('戰鬥結束，你死了')
            print('you lost ',d,' dollars')
            money -= d
            status[0] = 0
            status[1] = player_blood
            status[2] = money
            return status
        else:
            continue


event=0
a= input('enter your name :')
stat = [1, 10, 0]
while True:
    c = int(input('你想做什麼?(1查看血量2查看錢3隨機事件4買東西5挑戰boss)'))
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
            stat = fighting(stat[1], stat[2], a)
            print('player life = %d, money = %d'%(stat[1], stat[2]))
        elif event == 4:
            print('what do you want?')
            buy = str(input('1回復魔法($15)2回復HP($10)q離開')
            if buy == 1:
                if money <= 14:
                    print('you do not have enough money')
                    pass
                else:
                    print('magic point recover 5')
                    money -=15
                    pass
            elif buy ==2:
                if money <=10:
                    print('you do not have enough money')
                    pass
                else:
                    print('hp recover 5')
                    money -= 10
                    pass
            elif buy == q:
                print('你已離開')
                pass
        elif event ==5:
            boss_fight
        else:
            pass