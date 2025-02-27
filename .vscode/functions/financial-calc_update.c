//andrea lugo, financial_calc_update.c
#include <stdio.h>

float use(char type[]) {
    float amount;
    printf("What is your %s amount?\n", type);
    scanf("%f", &amount);
    return amount;
}

void word(float income, float amount, char type[]) {
    float percent = (amount / income) * 100;
    printf("You are spending $%.2f on %s, which is %.2f%% of your income.\n", amount, type, percent);
}

int main(void) {
    printf("Welcome to the Financial Calculator!\n");

    float income = use("income");
    float rent = use("rent");
    float utilities = use("utilities");
    float groceries = use("groceries");
    float transportation = use("transportation");

    float savings = income * 0.10;

    float spending = rent + utilities + groceries + transportation;

    word(income, rent, "rent");
    word(income, utilities, "utilities");
    word(income, groceries, "groceries");
    word(income, transportation, "transportation");

    printf("You are saving $%.2f, which is 10%% of your income.\n", savings);
    printf("Your total spending is $%.2f, excluding savings.\n", spending);

    return 0;
}