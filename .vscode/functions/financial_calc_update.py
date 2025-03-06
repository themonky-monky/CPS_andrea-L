# Andrea lugo, financial calculator python program

# write a print statement telling the user what the program is (budget calculator)

print("hello and welcome to your financial pcalculator\n")
# Ask for monthly income (user input)
pincome = float (input("what is your monthly income\n"))
#Ask for rent amount (user input)
prent = float (input("what is your monthly rent\n"))
#Ask for utilities amount (user input)
putilities = float (input("what is your monthly utilities\n"))
#Ask for groceries amount (user input)
pgroceries = float (input("what is your monthly groceries\n"))
#Ask for transportation amount (user input)
ptransportation = float (input("what is your monthly transportation\n"))
# calculator saving as 20% of income (variable)
psaving = pincome * 0.20
# calculator spending money income - (rent+utilities+groceries+transportation+savings) (variable)
pexpenses = prent + putilities + pgroceries + ptransportation + psaving
pspending = pincome - pexpenses


def percent(type, amount):
    percentage = amount / pincome * 100
    return f"you spend \${amount:.2f} on {type}, which is {percentage:.2f}% of your income"

print(f"Your monthly income is ${pincome:.2f}\n")
print(f"Your total monthly expenses are ${pexpenses:.2f}\n")
print(f"Your monthly savings are ${psaving:.2f}\n")
print(f"Your monthly spending money is ${pspending:.2f}\n")
print(f"your monthly rent is ${prent:.2f}\n")
print(f"your monthly utilities are ${putilities:.2f}\n")
print(f"your monthly groceries are ${pgroceries:.2f}\n")
print(f"your monthly transportation is ${ptransportation:.2f}\n")
print(percent("rent", prent))
print(percent("utilities", putilities))
print(percent("groceries", pgroceries))
print(percent("transportation", ptransportation))
print(percent("savings", psaving))
print(percent("spending money", pspending))