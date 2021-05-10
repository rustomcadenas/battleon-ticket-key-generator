import random 
from datetime import date

today = date.today()
d4 = today.strftime("%b-%d-%Y") 

fileCreateUniqueID = random.randint(100000, 999999)

file = open(d4 +"-"+ str(fileCreateUniqueID) +".txt", "w+")
 
generateRange = int(input("Enter Number of Copies: "))

for x in range(generateRange):  
    randomID = random.randint(100000, 999999)
    randomPass = random.randint(100000, 999999)

    file.write(str(randomID) +" "+ str(randomPass) + "\n")  




