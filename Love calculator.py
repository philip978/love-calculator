

print("welcome to the love calculator!")
name1 = input("what is your name?\n")
name2 = input("what is their name?\n")
word = name1 + name2
check1 = word.lower().count("t") + word.lower().count("r") + word.lower().count("u") + word.lower().count("e")
check2 = word.lower().count("l") + word.lower().count("o") + word.lower().count("v") + word.lower().count("e")
x = str(check1) + str(check2)
if int(x) < 10 or int(x) > 90:
    print(f"your score is {x},you go together like coke and mentos ")
elif 40 < int(x) < 50:
    print(f"your score is {x},you are alright together")
else:
    print(f"your score is {x}")
