import random as r
import time as t
def event1(hp):
    hpp = r.randint(1,3)
    hp+=hpp
    print('你回復了%d生命,你現在的生命是%d'%(hpp,hp))
    return hp
def event2(money):
    moneyy=r.randint(10,30)
    money=money+moneyy
    print('你撿到了%d塊錢,你現在有%d塊錢'%(moneyy,money))
    return money
def event3(hp,money,magic,skill):
    bedman_hp=r.randint(2,10)
    while True:
        art=r.randint(1,3)
        maggc=int(input('請問你是否要選擇魔攻1.是2.否'))
        if maggc==1:
            if magic>=2:
                if skill==0:
                    mag=r.randint(4,8)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(1)
                if skill==1:
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
                    mag=r.randint(1,2)
                    print('你打了壞人%d滴血'%(mag))
                    bedman_hp-=mag
                    print('壞人剩下%d滴血'%(bedman_hp))
                    t.sleep(0.5)
        elif maggc==2:
            print('你打了壞人%d滴血'%(art))
            bedman_hp-=art
            print('壞人剩下%d滴血'%(bedman_hp))
            t.sleep(1)
        if bedman_hp>0:
            hp-=1
            print('你剩下%d滴血'%(hp))
            t.sleep(1)
        elif bedman_hp<1:
            print('you kill bad man')
            monery=r.randint(10,20)
            money+=monery
            print('你得到了%d元，你現在有%d元'%(monery,money))
            break
    return hp,money,magic,skill
def store(money,hp,magic):
    if money>=99:
        m=input('請選擇你要購買的物品1.生命藥水2.魔法藥水3.魔法技能4.q離開')
        print(m)
        if m!='q':
            int(m)
            if m==1:
                print('你花100塊購買生命藥水')
                hp+=r.randint(3,6)
                print('你回復的生命')
                money-=100
            elif m==2:
                print('你花100塊購買魔法藥水')
                magic+=r.randint(5,8)
                money-=100
            elif m==3:
                mo=int(input('請輸入你想要購買的技能(只要在購買下一次前一個技能就會被刷新)1.流星雨2.龍捲風3.分身斬'))
                if mo==1:
                    money-=100
                    skill=1
                if mo==2:
                    if money>=150:
                        money-=150
                        skill=2
                if mo==3:
                    if money>=200:
                        money-=200
                        skill=3
        elif m=='q':
            print('你來到了商店')
    return money,hp,magic
question=str(input('輸入go即可開始遊戲'))
if question=='go':
    HP=10
    money=0
    magic=2
    skill=0
    while True:
        game=r.randint(1,4)
        if game==1:
            HP=event1(HP)
            game=r.randint(1,4)
        if game==2:
            money = event2(money)
            game=r.randint(1,4)
        if game==3:
            HP,money,magic,skill=event3(HP,money,magic,skill)
            game=r.randint(1,4)
        if game==4:
            money,HP,magic=store(money,HP,magic)
            game=r.randint(1,4)
        if HP<1:
            print('you died')
            break