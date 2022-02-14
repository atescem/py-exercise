import random

zar1 = random.randint(1,6)
zar2 = random.randint(1,6)

user1 = int(input("1. Kullanıcı tahmini: "))
user2 = int(input("2. Kullanıcı tahmini: "))

toplam = zar1 + zar2

fark1 = toplam - user1
fark2 = toplam - user2

if fark1 > fark2:
    print("Kullanıcı 1 Kazandı")

elif fark2 > fark1:
    print("Kullanıcı 2 Kazandı")

else:
    print("Kazanan Yok")