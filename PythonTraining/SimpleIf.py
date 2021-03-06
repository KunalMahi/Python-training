import datetime
DOB=input("Enter your Date of Birth :")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
if(Age>18):
    print("Your Age is {} and you are ana adult".format(Age))
if(Age<18):
    print("Your Age is {} and you are not ana adult".format(Age))