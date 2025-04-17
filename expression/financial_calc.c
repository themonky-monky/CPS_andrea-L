//andrea lugo, financial_calc.c
    #include <stdio.h>   
    
int main(void){

    float income, rent, utilities, groceries, transportation, saving, expenses, total;  
float prent, puntilities, pgroceries, ptransportation, psaving, pexpenses;  
printf("Hello and welcome to our financial calculator.\n");  
printf("How much do you make each month? ");  
scanf("%f", &income);  
printf("Your monthly income is $%.2f\n", income);   
printf("How much is your rent? ");  
scanf("%f", &rent);   
printf("How much are your utilities? ");  
scanf("%f", &utilities);  
printf("How much are your groceries? ");  
scanf("%f", &groceries);  
printf("How much is your transportation? ");  
scanf("%f", &transportation);  
expenses = rent + utilities + groceries + transportation;  
saving = income * 0.2;   
 total = income - expenses - saving;  
printf("Your monthly expenses are $%.2f\n", expenses);  
printf("Your monthly savings are $%.2f\n", saving);  
printf("You have $%.2f remaining after expenses and savings.\n", total);  
prent = (rent / income) * 100;  
puntilities = (utilities / income) * 100;  
pgroceries = (groceries / income) * 100;  
ptransportation = (transportation / income) * 100;  
pexpenses = (expenses / income) * 100;  
psaving = (saving / income) * 100;   
printf("Your rent is %.1f%% of your income.\n", prent);  
printf("Your utilities are %.1f%% of your income.\n", puntilities);  
printf("Your groceries are %.1f%% of your income.\n", pgroceries);  
printf("Your transportation is %.1f%% of your income.\n", ptransportation);  
printf("Your expenses are %.1f%% of your income.\n", pexpenses);  
printf("Your savings are %.1f%% of your income.\n", psaving);  

return 0; 
}