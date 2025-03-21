# Andrea lugo, financial calculator python program

def get_user_input():
    pincome = float(input("What is your monthly income?\n"))
    prent = float(input("What is your monthly rent?\n"))
    putilities = float(input("What are your monthly utilities?\n"))
    pgroceries = float(input("What are your monthly groceries?\n"))
    ptransportation = float(input("What is your monthly transportation?\n"))
    print_results(pincome, prent, putilities, pgroceries, ptransportation)    

def calculate(pincome, prent, putilities, pgroceries, ptransportation):  
    pexpenses = prent + putilities + pgroceries + ptransportation  
    psaving = pincome - pexpenses  
    return pexpenses, psaving  
def percent(category, amount, total):
    if total == 0:
        return f"You spent \\${amount:.2f} on {category}, which is 0% of your income."
    return f"You spent \\${amount:.2f} on {category}, which is {amount / total:.0%} of your income."

def print_results(pincome, pexpenses, psaving, prent, putilities, pgroceries, ptransportation):
    (f"Your total expenses are: \\${pexpenses:.2f}")
    print(f"Your total savings are: \\${psaving:.2f}")
    print(percent("rent", prent, pincome))
    print(percent("utilities", putilities, pincome))
    print(percent("groceries", pgroceries, pincome))
    print(percent("transportation", ptransportation, pincome))
    print(percent("savings", psaving, pincome))
  
def main():  
    print("Welcome to the budget calculator!")  
    pincome, prent, putilities, pgroceries, ptransportation = get_user_input()    
    pexpenses, psaving = calculate(pincome, prent, putilities, pgroceries, ptransportation)   
    print_results(pincome, pexpenses, psaving, prent, putilities, pgroceries, ptransportation)  
  
# Run the program  
main()