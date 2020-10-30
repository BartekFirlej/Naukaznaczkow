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



mycursor.close()
mydb.close()


