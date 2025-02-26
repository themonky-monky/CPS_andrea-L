#andrea lugo, old_enough.py
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to vote and drive.")
elif age >= 16:
    print("You are old enough to get a learner's permit and drive.")
elif age >= 5:
    print("You are old enough to go to school.")
else:
    print("You are not old enough to vote, drive, get a learner's permit, or go to school.")