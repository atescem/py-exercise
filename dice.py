import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

user1 = int(input("1. Kullanıcı tahmini: "))
user2 = int(input("2. Kullanıcı tahmini: "))

total = dice1 + dice2

odds1 = total - user1
odds2 = total - user2

if odds1 > odds2:
    print("Kullanıcı 1 Kazandı")

elif odds2 > odds1:
    print("Kullanıcı 2 Kazandı")

else:
    print("Kazanan Yok")