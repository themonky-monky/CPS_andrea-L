#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
# Ask for monthly income (user input)
income = float(input("what is your monthy income? $")) 
#Ask for rent amount (user input)
rent = float(input("what is your monthy rent\n")) 
#Ask for utilities amount (user input)
utilities = float(input("what is your monthy utilities\n"))
#Ask for groceries amount (user input)
groceries  = float(input("what is your monthy groseries\n"))
#Ask for transportation amount (user input)
transportation = float(input("what is your monthy transportation\n"))
# calculation savings as 10% of income (variable)
saving = income *0.10
# calculation spending money income - (rent+utilities+groceries+transportation+savings) (variable)
spending = ("rent + utilities + groceries + transportation + savings")

print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Utilities: ${utilities:.2f}")
print(f"Groceries: ${groceries:.2f}")
print(f"Transportation: ${transportation:.2f}")
print(f"Savings (10% of income): ${saving:.2f}")
print(f"Total Spending: ${spending:.2f}")