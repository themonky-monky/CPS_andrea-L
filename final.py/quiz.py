#Gavin Woodhouse, Tatiana Susov, Andrea Lugo, Ali Walton, Quiz
# Official final programming game title = Super-Duper Easy Quiz
print("Hello and welcome to this veeeery easy trivia quiz! Type in your answers and try to get all 10 questions correct.\n")
score = 0
asked_1 = 0
asked_2 = 0
asked_3 = 0
asked_4 = 0
asked_5 = 0
asked_6 = 0
asked_7 = 0
asked_8 = 0
asked_9 = 0
asked_10 = 0
asked_11 = 0
asked_12 = 0
asked_13 = 0
asked_14 = 0
asked_15 = 0
asked_16 = 0
asked_17 = 0
asked_18 = 0
asked_19 = 0

#Function for questions, Gavin
def question(prompt):
    return input(f"{prompt}?\n").strip().lower()

#Conditional to say whether answer to question was correct or not, Tatiana
def answer(correct1, correct2, correct3):
    global score
    if guess == correct1 or guess == correct2 or guess == correct3:
        print("Correct!\n")
        score +=1      
    else:
        print("Incorrect!\n")

#Loop to print questions with a random function, Ali
#Adds to the score and writes answers, Andrea
import random

num = 1
while num < 10:
    rand = random.randint(1,19)
    if rand == 1 and asked_1 == 0:
        guess = question("Can you tell me the time")
        answer("yes", "the time", "time for you to get a watch")
        asked_1 = 1
        num +=1
    
    elif rand == 2 and asked_2 == 0:
        guess = question("What was his name-o")
        answer("bingo", "b i n g o", "bluey")
        asked_2 = 1
        num +=1
    
    elif rand == 3 and asked_3 == 0:
        guess = question("If you had a speech impediment/disorder (ex: lisp, stuttering, dyslexia), how would you pronounce it")
        answer("lithp", "stutututtering", "lysdexia")
        asked_3 = 1
        num +=1

    elif rand == 4 and asked_4 == 0:
        guess = question("I feel like giving you a freebie, just type whatever, I guess")
        answer("whatever", "whatever, i guess", "whatever i guess")
        asked_4 = 1
        num +=1
        
    elif rand == 5 and asked_5 == 0:
        guess = question("What is 2 + 2 (Hint: 4 is not an answer)")
        answer("22", "an equation", "fish")
        asked_5 = 1
        num +=1

    elif rand == 6 and asked_6 == 0:
        guess = question("What little thing did Mary Have")        
        answer("lamb", "a lamb", "a little lamb")
        asked_6 = 1
        num +=1
    
    elif rand == 7 and asked_7 == 0:
        guess = question("If you are eating dumplings, what country would you likely be in")
        answer("china", "korea", "asia")
        asked_7 = 1
        num +=1

    elif rand == 8 and asked_8 == 0:
        guess = question("What continent would you find Togo in")
        answer("africa", "africa", "africa")
        asked_8 = 1
        num +=1

    elif rand == 9 and asked_9 == 0:
        guess = question("1,2,3,5,8,13,21,34___; what's the last number")
        answer("55", "55", "55")
        asked_9 = 1
        num +=1

    elif rand == 10 and asked_10 == 0:
        guess = question("If the answer to a question was '24 hours', what would the question be")
        answer("how long is a day", "what is the length of a day", "how many hours are in a day")
        asked_10 = 1
        num +=1

    elif rand == 11 and asked_11 == 0:
        guess = question("nuf gnivaH")
        answer("sey", "on", "ebyam")
        asked_11 = 1
        num +=1
        
    elif rand == 12 and asked_12 == 0:
        guess = question("What is the second letter of the alphabet plus the fifteenth letter of the alphabet times two")
        answer("boo", "b o o", "b + o x 2")
        asked_12 = 1
        num +=1
        
    elif rand == 13 and asked_13 == 0:
        guess = question("What thing do people usually argue over whether it is a string instrument or not")
        answer("piano", "bass", "a piano")
        asked_13 = 1
        num +=1

    elif rand == 14 and asked_14 == 0:
        guess = question("How do you spell tacocat backwards")
        answer("tacocat", "t a c o c a t", "sdrawkcab tacocat")
        asked_14 = 1
        num +=1
        
    elif rand == 15 and asked_15 == 0:
        guess = question("Are you a robot")
        answer("no", "maybe", "wouldn't you like to know")
        asked_15 = 1
        num +=1

    elif rand == 16 and asked_16 == 0:
        guess = question("What's your name? (don't actually tell me) How do you spell it")
        answer("it", "i t", "")
        asked_16 = 1
        num +=1

    elif rand == 17 and asked_17 == 0:
        guess = question("If you have lived for 1095 days, how old would you be")
        answer("3", "3 years old", "1095 days")
        asked_17 = 1
        num +=1

    elif rand == 18 and asked_18 == 0:
        guess = question("Type in nothing, please")
        answer("", "nothing", "nothing, please")
        asked_18 = 1
        num +=1

    elif rand == 19 and asked_19 == 0:
        guess = question("Before you read the rest of this question, read the emancipation proclamation. What color was the author's eyes")
        answer("hazel", "gray", "hazel gray")
        asked_19 = 1
        num +=1
        
    else:
        rand = random.randint(1,19)

guess = int(input(f"Last question! What is your score (ex: 7)?\n"))
if guess == score or guess == score+1:
    print("That's it!\n")
    score +=1      
else:
    print("So close!\n")

# Keeping track of the score to print what it is after answering the questions(Tells player how many they gott correct)
if score == 10:
    print(f"You got all correct, you're really smart!")
elif score == 9:
    print(f"You only missed one question, you smartie pants!")
elif score == 8:
    print(f"You got 8 out of the ten questions correct! Hey not bad.")   
elif score == 7:
    print(f"You got seven questions correct! Nice job!")
elif score == 6:
    print(f"You got six questions correct! You were so close!")
elif score == 5:
    print(f"You got 50% of questions correct! So close, yet so far.")
elif score == 4:
    print(f"You got four out of ten questions correct, you did good, some of the time.")
elif score == 3:
    print(f"You got three out of ten questions correct, thats 1/3, better than 1/4!")
elif score == 2:
    print(f"You got two out of ten questions correct, that's 20% which is pretty good.")
elif score == 1:
    print(f"Only one question correct out of ten, nice try.")
else:
    print(f"You got zero questions correct! You must be a genius and intentionally got all these incorrect, if not, you still did good, thank you for trying.")