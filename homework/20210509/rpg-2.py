import time
import random
a = str(input('enter your name'))
def update_life(status: list):
    get_life = random.randint(1, 3)
    status[1] += get_life
    print("Recovry Life = %d Your life = %d" % (get_life, status[1]))
    return status
def update_money(status: list):
    get_money = random.randint(10, 30)
    status[2] += get_money
    print("Get Money = %d Your Money = %d" % (get_money, status[2]))
    return status
def fighting(status: list):
    s = 0.5  # attack speed
    monster_life = random.randint(2, 10)
    print("Monster Life = %d" % monster_life)
    while True:
        while True:
            act = input("Use Magic Attack? y/n: ")
            if (act == 'y' and status[3] > 1):
                attack = random.randint(4, 10)
                status[3] -= 1
                print('player',a,'uses magical attack')
                break
            elif act == 'n':
                attack = random.randint(1, 3)
                print('player',a,'uses physical attack')
                break
        print("You make damage %d" % attack)
        monster_life -= attack
        time.sleep(s)
        print("Monster Life %d" % monster_life)
        if (monster_life < 1):
            print('player',a," beats monster")
            status[2] += random.randint(10, 20)
            return status
        else:
            print("Monster Attack")
            status[1] -= 1
            time.sleep(s)
            print("You hurt, Life = %d" % status[1])
            if (status[1] < 1):
                print('player',a,"dead")
                status[0] = 0
                return status
def store(status: list):
    while True:
        if (status[2] < 100):
            print("Money is not enough, quit store ")
            break
        act = input("What do you want to buy 'l'/life, 'm'/magic, 'q'/quit:")
        if (act == 'q'):
            print("88")
            break
        elif (act == 'l'):
            status[1] += random.randint(1, 3)
            status[2] -= 100
            print("Life=%d, Money=%d" % (status[1], status[2]))
        elif (act == 'm'):
            status[3] += random.randint(1, 3)
            status[2] -= 100
            print("Magic=%d, Money=%d" % (status[3], status[2]))
        else:
            continue
    return status
#main programe
sts = [1, 10, 0, 10]  #是否生存/HP/錢/MP
event_list = [update_life, update_money, fighting, store]
while True:
    rev = input("Do you want 'c' continue 'q' quit the game:")
    if (rev == "c"):
        sts = event_list[random.randint(0, len(event_list) - 1)](sts)
        if (sts[0] == 0):
            print("Game Over")
            break
        print("[[life = %d, money = %d, MP = %d]]" % (sts[1], sts[2], sts[3]))
    elif (rev == "q"):
        print("88")
        break
    else:
        continue