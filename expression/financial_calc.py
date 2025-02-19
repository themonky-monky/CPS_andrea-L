# Andrea lugo, financial calculator python

# write a print statement telling the user what the program is (budget calculator)

# Ask for monthly income (user input)
income = float(input("what is your monthy income? $")) 
#Ask for rent amount (user input)
rent = float(input("what is your monthy rent rent? $")) 
#Ask for utilities amount (user input)
utilities = float(input("what is your monthy utilities? $"))
#Ask for groceries amount (user input)
groceries  = float(input("what is your monthy groseries? $"))
#Ask for transportation amount (user input)
transportation = float(input("what is your monthy transportation? $"))
# calculation savings as 10% of income (variable)
saving = income *0.10
# calculation spending money income - (rent+utilities+groceries+transportation+savings) (variable)
spending_money = ("rent + utilities + groceries + transportation + savings")
# Calculate spending money as income minus (expenses + savings)
spending_money = income - (saving)
# calculation percent of rent (rent/income) (variable)
rent_percent = (rent/income)*100
# calculation ercent of utilities (utilities/income) (variable)
utilities_percent = (utilities/income)*100
# calculation percent of groceries (groceries/income) (variable)
groceries_percent = (groceries/income)*100 
# calculation percent of transportation (transportation/income) (variable)
transportation_percent = (transportation/income)*100
#calculator percet of saving (saving/income) (variable)
saving_percent = (saving/income)*100
#calculator percent of speding (speding/income) (variable)
spending_money_percent = (spending_money/income)*100
# tell user category spending amount AND percent for rent 100 ("you spend $xx% on rent that is xx% of your income")
print(f"You spend ${rent} on rent, which is (rent_percent:.2f)% of your income")
# tell user category spending amount AND percent for utilities 100 ("you spend $xx% on utilities that is xx% of your income")
print(f"You spend ${utilities} on utilities, which is (utilities_percent:.2f)% of your income")
# tell user category spending amount AND percent for groceries 100 ("you spend $xx% on groceries that is xx% of your income")
print(f"You spend ${groceries} on groceries, which is (groceries_percent:.2f)% of your income")
# tell user category spending amount AND percent for transportation 100( "you spend $xx% on transportation that is xx% of your income")
print(f"You spend ${transportation} on transportation, which is (transportation_percent:.2f)% of your income")
# tell user category spending amount AND percent for savings 100 ("you spend $xx% on savings that is xx% of your income")
print(f"You save ${saving} each month, which is (savings_percent:.2f)% of your income")
# tell user category spending amount AND percent for spending  100 ("you spend $xx% on spending that is xx% of your income")
print(f"You have ${spending_money}remaining for other spending, which is (spending_percent:.2f)% of your income") 