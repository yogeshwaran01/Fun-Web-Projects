finder=input("serach:")

file=open("me.txt")
count=0
for line in file:
    count+=1
    
    found=line.find(finder)
    if found==-1:
        pass
    else:
        print(line.strip())

print("this file has {ount} lines".format(ount=count))

