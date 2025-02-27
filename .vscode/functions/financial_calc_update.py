#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
income = float(input("what is your monthy income? $")) 
rent = float(input("what is your monthy rent rent? $")) 
utilities = float(input("what is your monthy utilities? $"))
groceries  = float(input("what is your monthy groseries? $"))
transportation = float(input("what is your monthy transportation? $"))
saving = income *.2
expenses = ("rent + utilities + groceries + transportation + savings")
spending = income-expenses-saving

prent = rent/income *100
putilities = utilities/income *100
pgroceries = groceries/income *100
ptransportation = transportation/income *100
psaving = saving/income *100
pexpenses = expenses/income *100
def percent(type, amount):
    per = amount/income *100
    
    return F"your {type} is {per}% income."

print(f"your montly income is ${income:.2f}\n")
print(f"your montly expenses is ${expenses:.2f}\n")
print(f"your montly saving is ${saving:.2f}\n")
print(f"your montly spending money is ${spending:.2f}\n")
print(percent("rent", rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("saving", saving))
print(percent("expenses", expenses))