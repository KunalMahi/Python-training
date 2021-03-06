word="Python"
for letter in word:
    print("{}".format(letter))
    if(letter=='t'):
        break;
for letter in word:
    if(letter=='t'):
        continue;
    print("{}".format(letter))

l={12,13,14,124,25,26}

for item in l:
    if(item==25):
        print("Number 25 is found")
        break;

print("App is done")