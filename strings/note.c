// andrea lugo, Strings Notes C
#include <stdio.h>
#include <string.h>

char name[20];

int main(void){
    //printf("please tell me your full name:\n");
    //scanf("%s", name);
    //fgets(name, 20, stdin); 
    //printf("Hello %s, welcome to my program", name);
    //char sentence[] = "The quck brown fox jumps over the lazy dog";
    //printf("%lu\n", strlen(sentence)); 
    char one[] = "hello "; 
    char two[] = "world!";
    char three[] = "this is my program. ";
    two[5] = '?';
    printf("%s\n", one); 
    strcat(one, two);
    printf("%s\n", one);
    strcat(three, one);
    printf("%s", three);
    return 0;
}