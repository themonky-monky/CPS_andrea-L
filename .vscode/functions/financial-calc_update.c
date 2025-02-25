//Andrea lugo, financial-calc-update.c
#include <stdio.h>
#include <math.h>

float income, rent, utilities, groceries, transportation, spending, savings;

// Condensed function to collect inputs
void collect_user_inputs() {
    printf("Enter your monthly income, rent, utilities, groceries, and transportation:\n");
    scanf("%f %f %f %f %f", &income, &rent, &utilities, &groceries, &transportation);
}

// Function to print a readable sentence for the user and calculate the percentage
void print_expense_summary(char* expense_name, float expense_amount) {
    float expense_percent = (expense_amount / income) * 100;
    printf("You spend $%.2f on %s, which is %.2f%% of your monthly income.\n", expense_amount, expense_name, expense_percent);
}

int main(void) {
    printf("Welcome to my financial calculator\n");

    collect_user_inputs();

    // Calculate savings (10% of income)
    savings = income * 0.10;
    spending = rent + utilities + groceries + transportation;

    // Print the expense summaries
    print_expense_summary("Rent", rent);
    print_expense_summary("Utilities", utilities);
    print_expense_summary("Groceries", groceries);
    print_expense_summary("Transportation", transportation);
    print_expense_summary("Total Spending", spending);
    print_expense_summary("Savings (10% of income)", savings);

    return 0;
}