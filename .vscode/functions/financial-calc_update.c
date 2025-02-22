//Andrea lugo, financial-calc-update.c
#include <stdio.h>
#include <math.h>
float income, rent, utilities, groceries, transportation, spending, savings;

void info(float income, float amount){
printf("%.2f%%\n", (income/amount)*100);

}
int main(void){
printf("welcome to my financial calculator\n");

printf("what is your monthy income?\n"); 
scanf("%f", &income);

printf   ("what is your monthy rent?\n");
scanf("%f", &rent);

printf("what is your monthy utilities?\n");
scanf("%f", &utilities);

printf("what is your monthy groceries?\n");
scanf("%f", &groceries);

printf("what is your monthy transportation?\n"); 
scanf("%f", &transportation);

savings = income *100;
float rent_percent = (rent/income)*100; 
float utilities_percent = (utilities/income)*100;
float groceries_percent = (groceries/income)*100;
float transportation_percent = (transportation/income)*100;
float spending = rent, utilities, groceries, transportation;
float spending_percent = (spending/income)*100;
float savings_percent = (savings/income)*100;

return 0;
}
