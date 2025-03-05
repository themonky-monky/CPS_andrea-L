# Andrea lugo, financial calculator python program

# write a print statement telling the user what the program is (budget calculator)

print("hello and welcome to your financial pcalculator\n")
# Ask for monthly income (user input)
income = float (input("what is your monthy income"))
#Ask for rent amount (user input)
rent = float (input("what is your monthy rent\n"))
#Ask for utilities amount (user input)
utilities = float (input("what is your monthy utilities\n"))
#Ask for groceries amount (user input)
groceries = float (input("what is your monthy groseries\n"))
#Ask for transportation amount (user input)
transportation = float (input("what is your monthy transportation\n"))
saving = income * 0.2
expenses = rent + utilities + groceries + transportation + saving
spending = income - expenses


def percent(type, amount):
    percentage = amount / income * 100
    return f"you spend \${amount:.2f} on {type}, which is {percentage:.2f}% of your income"

print(f"Your monthly income is ${income:.2f}\n")
print(f"Your total monthly expenses are ${expenses:.2f}\n")
print(f"Your monthly savings are ${saving:.2f}\n")
print(f"Your monthly spending money is ${spending:.2f}\n")
print(percent("rent", rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("saving", saving))
print(percent("expenses", expenses)) 