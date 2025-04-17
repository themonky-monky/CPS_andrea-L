# Andrea lugo, financial calculator python program

def get_user_inputs():
    
    try:
        income = float(input("Enter your monthly income: $"))
        expenses = {}
        print("Enter your expenses. Type 'done' when finished.")
        
        while True:
            category = input("Expense category: ").strip().lower()
            if category == 'done':
                break
            try:
                amount = float(input(f"Amount for {category}: $"))
                expenses[category] = amount
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        return income, expenses
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_user_inputs()

def calculate_percentages(income, expenses):
   
    print("\n--- Budget Breakdown ---")
    for category, amount in expenses.items():
        percentage = (amount / income) * 100 if income > 0 else 0
        print(f"{category.capitalize()}: ${amount:.2f} ({percentage:.0f}%)")

    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    savings_percentage = (savings / income) * 100 if income > 0 else 0
    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Savings: ${savings:.2f} ({savings_percentage:.0f}%)\n")

def main():
    """
    Main function to run the budget calculator.
    """
    print("Welcome to the Budget Calculator!")
    income, expenses = get_user_inputs()
    calculate_percentages(income, expenses)

# Run the program
if __name__ == "__main__":
    main()