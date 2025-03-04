#andrea lugo, loops notrd python

# 1. What is a loop? 
    #A Section of code that is going to repeat
# 2. What are the two types of loops?
    #Wile loop
x = 0
while x < 10:
    print("hello", x)
    x += 1

    #for loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)
# 3. What is iteration
    #The act of repeting something 

# 4. What are lists? 
    #A bunch of values in the same variable 
siblings = ["alex","katie", "andrew","vienna","tori","treyson"]
#print one item from the list 
print(siblings[3])
#change an item in a list
siblings[7] = "jake"
#remove an item from the list
siblings.pop(5)

# 5. How do you make lists in python? 
    # [] around the list, between each item in the list 
    # list items must be proper data types

# 6. How do you make for loops in python? 
#proper list priting with a for loop
for sibling in siblings:
    print(f"{num}.  {sibling} andrea")
    num +=1
#using range instead of a list
    for num in range(1,11,2):
        print(num)

# 7. How do you make while loops in python?
import random

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print(f"goose!")
        break #tells loops to be done
    else:
        print("duck")
    num += 1

    # continue tells the loop to stop that iteration and start again