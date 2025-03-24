# Andrea lugo, financial calculator python program

def get_user_input():
    income = float(input("What is your monthly income?\n"))
    rent = float(input("What is your monthly rent?\n"))
    utilities = float(input("What are your monthly utilities?\n"))
    groceries = float(input("What are your monthly groceries?\n"))
    transportation = float(input("What is your monthly transportation?\n"))
    return income, rent, utilities, groceries, transportation

def calculate(income, rent, utilities, groceries, transportation):
    expenses = rent + utilities + groceries + transportation
    savings = income - expenses
    return expenses, savings

def percent(category, amount, total):
    if total == 0:
        return f"You spent ${amount:.2f} on {category}, which is 0% of your income."
    return f"You spent ${amount:.2f} on {category}, which is {amount / total:.0%} of your income."

def print_results(income, rent, utilities, groceries, transportation):
    expenses, savings = calculate(income, rent, utilities, groceries, transportation)
    print(f"Your total expenses are: ${expenses:.2f}")
    print(f"Your total savings are: ${savings:.2f}")
    print(percent("rent", rent, income))
    print(percent("utilities", utilities, income))
    print(percent("groceries", groceries, income))
    print(percent("transportation", transportation, income))
    print(percent("savings", savings, income))

def main():
    print("Welcome to the budget calculator!")
    income, rent, utilities, groceries, transportation = get_user_input()
    print_results(income, rent, utilities, groceries, transportation)

# Run the program
main()