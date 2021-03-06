listItems=[1,2,3,4,5,6,7]
tempList=[]
for item in listItems:
    tempList.append(item*2)
print(tempList)

templist2=list(map(lambda x:x*2 , listItems))
print(templist2)

templist3=list(map(lambda x:x+3 , listItems))
print(templist3)
