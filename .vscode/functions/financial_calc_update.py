#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
print("Welcome to the Budget Calculator!\n")

# Ask for monthly income (user input)
income = float(input("What is your monthly income? $")) 

# Ask for rent amount (user input)
rent = float(input("What is your monthly rent? $")) 

# Ask for utilities amount (user input)
utilities = float(input("What is your monthly utilities? $"))

# Ask for groceries amount (user input)
groceries = float(input("What is your monthly groceries? $"))

# Ask for transportation amount (user input)
transportation = float(input("What is your monthly transportation? $"))

# Calculate savings as 10% of income
saving = income * 0.10

# Calculate total spending (sum of rent, utilities, groceries, transportation, and savings)
spending = rent + utilities + groceries + transportation + saving

# Display the breakdown
print(f"\nIncome: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Utilities: ${utilities:.2f}")
print(f"Groceries: ${groceries:.2f}")
print(f"Transportation: ${transportation:.2f}")
print(f"Savings (10% of income): ${saving:.2f}")
print(f"Total Spending: ${spending:.2f}")

income, rent, utilities, groceries, transportation
saving = (income)
spending = (rent, utilities, groceries, transportation, saving)
(income, rent, utilities, groceries, transportation, saving, spending)