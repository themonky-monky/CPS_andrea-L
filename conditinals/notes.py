# andrea lugo, conditinals notes python

#print("hello, welcome to my progrma that will sort you into a category.")

#name = input("what is your name:\n")

#if name == "andrea":
    #print("oh your the teacher...never mind.")
#else:
    #print("you are a student. welcome to class.")


"""
num = num = int(input("how many would you like:(give me a nunber above 0)\n"))

if num == 1:
    print("you have asked for a item")
elif num <= 3:
    print("you have asked for a couple of the item.")
elif num <= 5:
    print("you have asked for a few of the item...or your in the south and you asked for a couple.")
else:
    print("you have asked for some of the item.")
"""
    
name = "katie"

if "a" in name or "e" in name or"i" in name or "o" in name or "u" in name:
    print("your name has a vowel!")
else:
    print("your name dosn't have a vowel.")

    num = 6 

if num > 5 and num < 10:
    if num == 7:
        print(f"{num}that is an unluck number!")
    else:
        print(f"{num}that is a large singles digit number")
else:
    if num == 4:
        print(f"{num} is the best number!")
    else:
        if num > 10:
            print(f"{num} is not a single digit number")
        else:
            print(f"{num} is a small number")