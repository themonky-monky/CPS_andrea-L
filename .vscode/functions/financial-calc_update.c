//andrea lugo, financial_calc_update.c
#include <stdio.h>
#include <math.h>
float income, rent, utilities, groceries, transportation, spending, savings;

float use(char type[]){
    float amount;
    printf("what is your %s amount?\n", type); 
    scanf("%f", &amount);
    return amount;
}

void word(float income, float amount){
    float percent = (amount/income)*100;
    printf("you are spending $%.2f this is %.2f%%", amount, percent);
}

int main(void){
printf("welcome to my financial calculator\n");



rent = use("rent");

utilities = use("utilities");

groceries = use("groceries");

transportation = use("transportation");

float spending = income - (rent + utilities + groceries + transportation);

float savings = income *100;

word(income, rent);
word(income, utilities);
word(income, groceries);
word(income, transportation);

printf("you are savings $%.2f this is 10%%", savings);
printf("you are spending $%.2f this is 10%%", spending);
return 0;
}