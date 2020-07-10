#FLAMES

name_1 = str(input("NAME:"))
name_2 = str(input("NAME:"))

def chop(name):
    lis = []
    for letter in name:
        lis.append(letter)
    return lis
        

n_1 = chop(name_1)
n_2 = chop(name_2)

for n in n_1:
    if n in n_2:
        n_1.remove(n)
        n_2.remove(n)


total = len(n_1) + len(n_2)

group = ["Friends","Lover","Affection","Marriage","Enemy","Sister"]

while len(group) > 1:
    index = ( total % len(group) - 1 )

    if index >= 0 : 
        right = group[index + 1 : ] 
        left = group[ : index] 
        group = right + left 
    else : 
        group = group[ : len(group) - 1] 
  

print(group[0])
