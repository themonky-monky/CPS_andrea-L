#andrea lugo, financial_calc_update.py

# write a print statement telling the user what the program is (budget calculator)
      
def collect_user_inputs():
    income = float(input("What is your monthly income? $")) 
    rent = float(input("What is your monthly rent? $")) 
    utilities = float(input("What is your monthly utilities? $"))
    groceries = float(input("What is your monthly groceries? $"))
    transportation = float(input("What is your monthly transportation? $"))
    return income, rent, utilities, groceries, transportation

# Function to calculate savings (10% of income)
def calculate_savings(income):
    return income * 0.10

# Function to calculate total spending
def calculate_total_spending(rent, utilities, groceries, transportation, savings):
    return rent + utilities + groceries + transportation + savings

# Function to display the breakdown of the budget
def display_budget(income, rent, utilities, groceries, transportation, savings, spending):
    print(f"\nIncome: ${income:.2f}")
    print(f"Rent: ${rent:.2f}")
    print(f"Utilities: ${utilities:.2f}")
    print(f"Groceries: ${groceries:.2f}")
    print(f"Transportation: ${transportation:.2f}")
    print(f"Savings (10% of income): ${savings:.2f}")
    print(f"Total Spending: ${spending:.2f}")

# Main function to run the program
def main():
    # Welcome statement
    print("Welcome to the Budget Calculator!\n")

    # Collect user inputs
    income, rent, utilities, groceries, transportation = collect_user_inputs()

    # Calculate savings
    savings = calculate_savings(income)

    # Calculate total spending
    spending = calculate_total_spending(rent, utilities, groceries, transportation, savings)

    # Display the budget breakdown
    display_budget(income, rent, utilities, groceries, transportation, savings, spending)

# Run the main function
if __name__ == "__main__":
    main()