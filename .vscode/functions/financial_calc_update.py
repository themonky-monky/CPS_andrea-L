# Andrea lugo, financial calculator python program

def calculate(income, **expenses):
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    return {'total_expenses': total_expenses, 'savings': savings}

def print_percentages(income, results, **expenses):
    for category, amount in expenses.items():
        percentage = (amount / income) * 100 if income > 0 else 0
        print(f"You spent ${amount:.2f} on {category}, which is {percentage:.0f}% of your income.")
    savings_percentage = (results['savings'] / income) * 100 if income > 0 else 0
    print(f"Your savings are ${results['savings']:.2f}, which is {savings_percentage:.0f}% of your income.")

def print_results(income, **expenses):
    results = calculate(income, **expenses)
    print(f"Your total expenses are: ${results['total_expenses']:.2f}")
    print(f"Your total savings are: ${results['savings']:.2f}")
    print_percentages(income, results, **expenses)

def main():
    print("Welcome to the budget calculator!")
    try:
        income = float(input("Enter your monthly income: $"))
        expenses = {
            'rent': float(input("Enter your monthly rent: $")),
            'utilities': float(input("Enter your monthly utilities: $")),
            'groceries': float(input("Enter your monthly groceries: $")),
            'transportation': float(input("Enter your monthly transportation: $"))
        }
        print_results(income, **expenses)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
# Run the program
main()
