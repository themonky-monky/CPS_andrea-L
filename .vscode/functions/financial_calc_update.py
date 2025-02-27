#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
def collect_user_inputs():
    income = float(input("What is your monthly income? $"))
    rent = float(input("What is your monthly rent? $"))
    utilities = float(input("What is your monthly utilities? $"))
    groceries = float(input("What is your monthly groceries? $"))
    transportation = float(input("What is your monthly transportation? $"))
    return income, rent, utilities, groceries, transportation

def calculate_percentage(income, rent, utilities, groceries, transportation):
    rent_percent = (rent / income) * 100
    utilities_percent = (utilities / income) * 100
    groceries_percent = (groceries / income) * 100
    transportation_percent = (transportation / income) * 100
    return rent_percent, utilities_percent, groceries_percent, transportation_percent

def display_budget(income, rent, utilities, groceries, transportation, rent_percent, utilities_percent, groceries_percent, transportation_percent):
    print(f"\nIncome: ${income:.2f}")
    print(f"Rent: ${rent:.2f} ({rent_percent:.2f}% of income)")
    print(f"Utilities: ${utilities:.2f} ({utilities_percent:.2f}% of income)")
    print(f"Groceries: ${groceries:.2f} ({groceries_percent:.2f}% of income)")
    print(f"Transportation: ${transportation:.2f} ({transportation_percent:.2f}% of income)")

def main():
    
    print("Welcome to the Budget Calculator!\nThis program helps you manage your monthly income and expenses.\n")

    income, rent, utilities, groceries, transportation = collect_user_inputs()

    rent_percent, utilities_percent, groceries_percent, transportation_percent = calculate_percentage(income, rent, utilities, groceries, transportation)

    display_budget(income, rent, utilities, groceries, transportation, rent_percent, utilities_percent, groceries_percent, transportation_percent)

if __name__ == "__main__":
    main()