#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
income = float(input("What is your monthly income? $")) 
rent = float(input("What is your monthly rent? $")) 
utilities = float(input("What are your monthly utilities? $"))
groceries = float(input("What are your monthly groceries? $"))
transportation = float(input("What is your monthly transportation cost? $"))

saving = income * 0.2
expenses = rent + utilities + groceries + transportation + saving
spending = income - expenses

prent = rent / income * 100
putilities = utilities / income * 100
pgroceries = groceries / income * 100
ptransportation = transportation / income * 100
psaving = saving / income * 100
pexpenses = expenses / income * 100

def percent(type, amount):
    per = amount / income * 100
    return f"Your {type} is {per:.2f}% of your income."

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