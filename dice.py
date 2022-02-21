import random
import sqlite3

def tryf():
    try:
        sqliteConnection = sqlite3.connect('dicedb.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to Database")

        sqlite_insert_query = "INSERT INTO data_main(name1, name2, dice1, dice2, guess1, guess2, winner) VALUES ('"+name1+"','"+name2+"','"+str(dice1)+"','"+str(dice2)+"','"+str(guess1)+"','"+str(guess2)+"','"+winner+"');"

        count = cursor.executescript(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into data_main table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
def finalf():
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")    



name1 = str(input("1. Kullanıcı, adınızı giriniz: "))
name2 = str(input("2. Kullanıcı, adınızı giriniz: "))

key = 1
while key == 1:

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    guess1 = int(input(name1 + "'in tahmini: "))
    guess2 = int(input(name2 + "'in tahmini: "))

    total = dice1 + dice2

    odds1 = total - guess1
    odds2 = total - guess2
    winner = "null"

    if odds1 < odds2:
        print("Kazanan: " + name1)
        winner = name1

    elif odds2 < odds1:
        print("Kazanan: " + name2)
        winner = name2

    else:
        print("Kazanan Yok")
        key = 0
        
    tryf()

#birinci function bir db ismi alıp db yi bağlantı atıcak ve vursor döndürecek .
#ikinci function bir cursor alıcak parametreleri alıcak ve insterleyecek.
   