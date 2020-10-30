import os
from datetime import datetime
from PIL import Image
import random
import mysql.connector

mydb = mysql.connector.connect(         #lacze sie z baza danych
    host="localhost",
    user="root",
    password="",
    database="obrazki"
    )
mycursor=mydb.cursor()

def importimages():
    mycursor.execute("TRUNCATE TABLE obrazy")                   #czysci tabele z pozostalosci
    pliki=os.listdir("obrazy")                                  #pobiera tablice z plikami w folderze obrazy
    for x in pliki:
        sql="INSERT INTO obrazy (nazwa, link) VALUES (%s, %s) " #zapytanie
        val=(x,x.split(".")[0])                                 #wartosci
        mycursor.execute(sql,val)                               #wykonanie
        mydb.commit()                                           #synchronizacja

def game_mode():                                                            #FUNKCJA POBIERAJACA ILOSC POWTORZEN ITP
    i = input("WITAJ. WYBIERZ CO CHCESZ ZROBIC: 1-GRA 2-UPDATE:   ")
    while not (i in ['1', '2']):
        i = input("WITAJ. WYBIERZ CO CHCESZ ZROBIC: 1-GRA 2-UPDATE:   ")
    if (int(i) == 2):
        importimages()                                                          #POBIERA OBRAZY Z FOLDERU I WRZUCA DO BAZY
        return 0
    else:
        i=input("ILE MA SIE UKAZAC ZNACZKOW?   ")
        while not i.isnumeric():
            i = input("ILE MA SIE UKAZAC ZNACZKOW?   ")
        return int(i)

def gra(ilosc):
    odp=0                                                                       #LICZNIK POPRAWNYCH ODP
    mycursor.execute("SELECT * FROM obrazy")                             #ZLICZA ILOSC OBRAZKOW W BAZIE
    wynik=mycursor.fetchall()                                           #ODBIERAM NAZWY OBRAZKOW
    for x in range(ilosc):                                                  #TYLE PYTAN ILE WYBRAL USER
        wszystkie=random.sample(wynik,4)                                    #LOSUJE 4 OBRAZKI
        dobra=random.sample(wszystkie,1)                                    #LOSUJE Z 4 TEN JEDEN DOBRY
        im=Image.open(str("obrazy/"+dobra[0][0]))                           #OTWIERAM DOBRY
        im.show()
        answer=wszystkie.index(dobra[0])                                    #BIORE CYFRE DOBREGO
        i = 1
        for y in wszystkie:
            print(str(i)+". "+y[1])                                         #WYPISUJE 4 ODPOWIEDZI I NUMERY
            i+=1
        a=int(input("Podaj odp 1,2,3,4 \n"))                                #CZEKAM NA ODP
        if (a==answer+1):
            print("DOBRA ODPOWIEDŹ MASZ PUNKT")                             #POROWNUJE I ZLICZAM PUNKTY
            odp+=1
        else:
            print("ŹLE POPRAWNA ODPOWIEDŹ: "+str(answer+1))
    print("ZDOBYLES: "+str(odp)+" PUNKTOW")



def main():
    ilosc_prob = game_mode()
    gra(ilosc_prob)



main()

mycursor.close()
mydb.close()


