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

def game_mode():
    i = input("WITAJ. WYBIERZ CO CHCESZ ZROBIC: 1-GRA 2-UPDATE:   ")
    while not (i in ['1', '2']):
        i = input("WITAJ. WYBIERZ CO CHCESZ ZROBIC: 1-GRA 2-UPDATE:   ")
    if (int(i) == 2):
        importimages()
        return 0
    else:
        i=input("ILE MA SIE UKAZAC ZNACZKOW?")
        while not i.isnumeric():
            i = input("ILE MA SIE UKAZAC ZNACZKOW?")
        return i



def main():
    ilosc_prob = game_mode()



main()

mycursor.close()
mydb.close()


