from time import sleep
import random

print("**************")
print("GUESS THE WORD")
print("**************")
print("            loading...          ")
sleep(6)
n = str(input("YOUR NAME PLEASE:"))

print("welcome ", n)

print("            loading...          ")
sleep(5)
anss = ""

modes = ["1)flower", "2)animals", "3)country", "4)states", "5)city"]
print("_________________")
print("select the type:")
print("_________________")
for mode in modes:
    print(mode)

flower = ["rose", "sunflower", "jasmine", "lily"]
animals = ["lion", "tiger", "elephant", "deer", "dear", "fox"]
country = ["spain", "america", "japan", "china", "germany"]
states = ["tamilnadu", "kerla", "goa"]
city = ["chennai", "mumbai", "delhi", ]

mode = input("select the mode:")

print("     loading word for you         ")
sleep(3)

if mode == "1":
    words = flower
elif mode == "2":
    words = animals
elif mode == "3":
    words = country
elif mode == "4":
    words = states
elif mode == "5":
    words = city
else:
    print("select the valid mode")

word = random.choice(words)

turns = len(word)

while turns > 0:
    out = 0
    for letter in word:
        if letter in anss:
            print(letter)
        else:
            print("_")
            out = out + 1
    if out == 0:
        print("_________________")
        print("you won", n)
        print("_________________")
        break

    ans = input("guess your letter")
    anss += ans
    if ans not in word:
        turns = turns - 1
        print(ans, " is wrong")
        if turns == 0:
            print("_________________")
            print("you loose", n)
            print("_________________")
            print("CORRECT ANSWER IS ", word.upper())
