# Andrea lugo, financial calculator python

# write a print statement telling the user what the program is (budget calculator)

# Ask for monthly income (user input)
income = float(input("what is your monthy income\n"))
#Ask for rent amount (user input)
rent = float(input("what is your monthy rent amount\n"))
#Ask for utilities amount (user input)
utilities = float(input("what is your monthy utilities\n"))
#Ask for groceries amount (user input)
graceries  = float(input("what is your monthy groseries\n"))
#Ask for transportation amount (user input)
transportation = float(input("what is your monthy transportation\n"))
# calculation savings as 10% of income (variable)
savings = income *0.10
# calculation spending money income - (rent+utilities+groceries+transportation+savings) (variable)
spending_money = income - ("rent + utilities + groceries + transportation + savings")
# calculation percent of rent (rent/income) (variable)
rent_percent = ("rent/income")*100
# calculation percent of utilities (utilities/income) (variable)
ultilities_percent = ("ultilities/income") *100
# calculation percent of groceries (groceries/income) (variable)
groceries_percent = ("groseries/income") *100
# calculation percent of transportation (transportation/income) (variable)
transportation_percent = ("transportation/income") *100
# tell user category spending amount AND percent for rent 100 ("you spend $xx% on rent that is xx% of your income")
print(f"You spend $(rent) on rent, which is (rent_percent:.2f)% of your income")
# tell user category spending amount AND percent for utilities 100 ("you spend $xx% on utilities that is xx% of your income")
print(f"You spend $(utilities) on utilities, which is (utilities_percent:.2f)% of your income")
# tell user category spending amount AND percent for groceries 100 ("you spend $xx% on groceries that is xx% of your income")
print(f"You spend $(groceries) on groceries, which is (groceries_percent:.2f)% of your income")
# tell user category spending amount AND percent for transportation 100( "you spend $xx% on transportation that is xx% of your income")
print(f"You spend $(transportation) on transportation, which is (transportation_percent:.2f)% of your income")
# tell user category spending amount AND percent for savings 100 ("you spend $xx% on savings that is xx% of your income")
print(f"You save $(savings) each month, which is (savings_percent:.2f)% of your income")
# tell user category spending amount AND percent for spending  100 ("you spend $xx% on spending that is xx% of your income")
print(f"You have $(spending_money)remaining for other spending, which is (spending_percent:.2f)% of your income") 