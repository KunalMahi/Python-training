import datetime
DOB=input("Enter your Date of Birth :")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(DOB)
print("Your Age is {}".format(Age))