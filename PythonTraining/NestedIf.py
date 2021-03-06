age=input("Enter Your age:")
if(int(age)>18):
    print("you are eligible for voting")
    if(int(age)>30):
        print("You are in Class A")
    else:
        print("You are in class B")
else:
    print("You are not eligible for voting")
print("App is done")