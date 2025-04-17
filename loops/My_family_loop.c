//andrea lugo, my family loop c 

#include <stdio.h>
int main(void){
    
    char *friends[] = {"Jake", "Olivia", "Sophia", "Liam", "James"};
    
    for(int i = 0; i < 5; i++) {
        printf("Hello, %s! How are you?\n", friends[i]);
    } 
    
    return 0; 
}