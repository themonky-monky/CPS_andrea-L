//andrea lugo,financial calculator
#include <studio.h>
int main(void){
    float income, rent, utilities, groceries, transportation, saving, expenses, total;
    float prent, puntilities, pgroceries, ptransportation, psaving, pexpenses, ptotal;
    Printf("hello and welcome to our financial_calculator\n");
    printf("how much do you make each month?");
    scanf("%f", &income);
    printf("your monthly icome is $%.2f\n", income); 
    scanf("%f", &rent);
    printf("how is your utilities?");
    scanf("%f", &utilities);
    print("how is your groseries?");
    scanf("%f", &rent);
    printf("yor monthly income is $%.2f\n", income);
    printf("how is your transportation?");
    scanf("%f", &transportation);
    expenses = rent + groceries + transportation;
    saving = income * .2;
    printf("your monthly income is $%.2f\n", income)
    printf("your monthly expenses are $%.2f\n", expenses);
    printf("your monthly saving are $%.2f\n", saving);
    printf("you have $%.2f\n", total);
    prent = rent/income *100;
    puntilities = utilities/income *100;
    pgroceries = groceries/income *100;
    ptransportation = transportation/income *100;
    pexpenses = expenses/income *100;
    psaving = saving/income *100/
    printf("your expenses are %.1f%% of your income\n", pexpenses);
    return 0;
}