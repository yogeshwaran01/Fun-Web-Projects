import time
mark_sheat={}
print("*********************************************************************")
print("rule:if you ones uploaded all subject and marks \n type 'submit' or 'done' \n format is sub=mark")
print("*********************************************************************")
print("ENTER THE SUBJECT=MARK")
print("_______________________")
while True:
    try:
        reply = str(input("->"))
        if reply=="done" or reply=="submit":
            break
        reps=reply.split("=")
        mark_sheat[reps[0]]=int(reps[-1])
    except:
        print("Invalid format;refer the rules")
        time.sleep(3)
        quit()

marks_list=list(mark_sheat.values())

average = sum(marks_list)/len(marks_list)

def submark():
    for sub,mark in mark_sheat.items():
            print("{}    | {}".format(sub,mark))

total = sum(marks_list)



def grades(average):
    if average > 95:
        grade="O"
        print("grade  |",grade)
    elif average > 85:
        grade="A"
        print("grade  |",grade)
    elif average > 75:
        grade="B"
        print("grade  |",grade)
    elif average > 65:
        grade="C"
        print("grade  |",grade)
    elif average > 35:
        grade="D"
        print("grade  |",grade)
    else:
        grade="FAIL"
        print("grade  |",grade)


submark()
print("total  |",total)
print("average|",average)
grades(average)

