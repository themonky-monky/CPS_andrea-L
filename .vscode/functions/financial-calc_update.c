//Andrea lugo, financial-calc-update.c
#include <stdio.h>
#include <math.h>
float income, rent, utilities, groceries, transportation, spending, savings;

void collect_user_inputs() {
printf("What is your monthly income?\n");
scanf("%f", &income);

printf("What is your monthly rent?\n");
scanf("%f", &rent);

printf("What is your monthly utilities?\n");
scanf("%f", &utilities);

printf("What is your monthly groceries?\n");
scanf("%f", &groceries);

printf("What is your monthly transportation?\n");
scanf("%f", &transportation);
}

// Function to print a readable sentence for the user
void print_expense_summary(char* expense_name, float expense_amount, float expense_percent){
printf("You spend $%.2f on %s, which is %.2f%% of your monthly income.\n", expense_amount, expense_name, expense_percent);
}

int main(void) {
printf("Welcome to my financial calculator\n");

collect_user_inputs();

// Calculate savings (10% of income)
savings = income * 0.10;

spending = rent + utilities + groceries + transportation;

float rent_percent = (rent / income) * 100;
float utilities_percent = (utilities / income) * 100;
float groceries_percent = (groceries / income) * 100;
float transportation_percent = (transportation / income) * 100;
float spending_percent = (spending / income) * 100;
float savings_percent = (savings / income) * 100;

print_expense_summary("Rent", rent, rent_percent);
print_expense_summary("Utilities", utilities, utilities_percent);
print_expense_summary("Groceries", groceries, groceries_percent);
print_expense_summary("Transportation", transportation, transportation_percent);
print_expense_summary("Total Spending", spending, spending_percent);
print_expense_summary("Savings (10% of income)", savings, savings_percent);

return 0;
}