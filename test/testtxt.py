from datetime import date
import random

today = date.today()

randomID = random.randint(100000, 999999)


d4 = today.strftime("%b-%d-%Y")

file = open(d4 +"-"+ str(randomID) +".txt", "w+")

file.write("Hello World")

file.close()