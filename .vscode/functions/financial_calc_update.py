# Andrea lugo, financial calculator python program

def budget_calculator():
    # Print a statement telling the user what the program is
    print("Hello and welcome to your financial budget calculator\n")
    
    # Use the helper function to ask for user inputs
    pincome = float(input("What is your monthly income?\n"))
    prent = float(input("What is your monthly rent?\n"))
    putilities = float(input("What is your monthly utilities?\n"))
    pgroceries = float(input("What is your monthly groceries?\n"))
    ptransportation = float(input("What is your monthly transportation?\n"))
    
    # Calculate savings as 20% of income
    psaving = pincome * 0.20
    
    # Calculate total expenses: rent + utilities + groceries + transportation + savings
    pexpenses = prent + putilities + pgroceries + ptransportation + psaving
    
    # Calculate spending money: income - total expenses
    pspending = pincome - pexpenses
    
    # Function to calculate and print the percentage of each expense
    def percent(type, amount):
        percentage = amount / pincome * 100
        return f"You spend ${amount:.2f} on {type}, which is {percentage:.2f}% of your income"
    
    # Output the results
    print(f"Your monthly income is ${pincome:.2f}")
    print(f"Your total monthly expenses are ${pexpenses:.2f}")
    print(f"Your monthly savings are ${psaving:.2f}")
    print(f"Your monthly spending money is ${pspending:.2f}")
    print(f"Your monthly rent is ${prent:.2f}")
    print(f"Your monthly utilities are ${putilities:.2f}")
    print(f"Your monthly groceries are ${pgroceries:.2f}")
    print(f"Your monthly transportation is ${ptransportation:.2f}")
    
    # Print percentage breakdown of each category
    print(percent("rent", prent))
    print(percent("utilities", putilities))
    print(percent("groceries", pgroceries))
    print(percent("transportation", ptransportation))
    print(percent("savings", psaving))
    print(percent("spending money", pspending))

# Call the function to run the budget calculator
budget_calculator()