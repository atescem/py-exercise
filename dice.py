import random

name1 = str(input("1. Kullanıcı, adınızı giriniz: "))
name2 = str(input("2. Kullanıcı, adınızı giriniz: "))

key = 1
while key == 1:

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    user1 = int(input(name1 + "'in tahmini: "))
    user2 = int(input(name2 + "'in tahmini: "))

    total = dice1 + dice2

    odds1 = total - user1
    odds2 = total - user2


    if odds1 > odds2:
        print("Kazanan: " + name1)

    elif odds2 > odds1:
        print("Kazanan" + name2)

    else:
        print("Kazanan Yok")
        key = 0