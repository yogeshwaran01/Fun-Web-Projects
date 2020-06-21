class Student:
    def __init__(self, name, tamil, english, maths, science, social):
        self.name = name
        self.tamil = tamil
        self.english = english
        self.maths = maths
        self.science = science
        self.social = social

    def average(self):
        print("*************************************")
        print("THE TOTAL AVERAGE OF ALL FIVE SUBJECT")
        print("total=", self.tamil + self.english + self.maths + self.science + self.social)
        return (self.tamil + self.english + self.maths + self.science + self.social) / 5

    def lang_average(self):
        print("*************************************")
        print("THE TOTAL AVERAGE OF LAUNGUAGE SUBJECT")
        print("tamil=", self.tamil)
        print("english=", self.english)
        print("total=", self.tamil + self.english)
        return (self.tamil + self.english) / 2

    def major_average(self):
        print("*************************************")
        print("THE TOTAL AVERAGE OF MAJOR SUBJECT")
        print("maths=", self.maths)
        print("science=", self.science)
        print("social=", self.social)
        print("total=", self.maths + self.science + self.social)
        return (self.maths + self.science + self.social) / 3

    def all(self):
        pass


nam = str(input("enter the student name:"))
tam = int(input("enter the tamil mark:"))
eng = int(input("enter the english mark:"))
mat = int(input("enter the maths mark:"))
sci = int(input("enter the science mark:"))
soc = int(input("enter the social mark:"))

print("_________________")
print("select the modes")
print("_________________")

modes = ["1)average", "2)average of language", "3)average of major", "4)all the above"]

for mode in modes:
    print(mode)

option = str(input("enter the mode number:"))

boss = Student(nam, tam, eng, mat, sci, soc)

if option == "1":
    print("average=", boss.average())
elif option == "2":
    print("average=", boss.lang_average())
elif option == "3":
    print("average=", boss.major_average())
elif option == "4":
    print("average=", boss.average())
    print("average=", boss.lang_average())
    print("average=", boss.major_average())

else:
    print("invalid mode")
