//andrea lugo, old enough c 
#include <stdio.h>
#include <string.h>

char name[] = "andrea"; 
int age; 

int main(void) {
    if(strcmp(name, "andrea") == 0){
        printf("hello andrea, welcome to class\n");
    } else {
        printf("Please enter your age: ");
        scanf("%d", &age); // Read the user's age
    
        // Check if the user meets any of the age conditions
        if (age >= 18) {
            printf("You are old enough to vote and drive.\n");
        } 
        else if (age >= 16) {
            printf("You are old enough to get a learner's permit and drive.\n");
        } 
        else if (age >= 5) {
            printf("You are old enough to go to school.\n");
        } 
        else {
            printf("You are not old enough to vote, drive, get a learner's permit, or go to school.\n");
        }
    }

    return 0; // Moved return 0 outside the else block
}
