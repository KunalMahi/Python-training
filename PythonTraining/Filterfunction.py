listItems=[1,2,3,4,5,6,7,8,9,10]
print(listItems)
tempList=[]
for item in listItems:
    if item%2==0:
        tempList.append(item)
print(tempList)

tempList2=list(filter(lambda x:x%2==0,listItems))
print(tempList)