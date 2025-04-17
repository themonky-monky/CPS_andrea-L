// andrea lugo, conditional notes c
#include <stdio.h>
#include <string.h>
char name[] = "andrea";

int num = 8;

int main(void){
    if(strcmp(name, "andrea") == 0){
    printf("hello andrea. welcome to class\n");
}else{
     printf("hello %s, welcome to class!\n", name);
}
// && = and
// || = or 
// != = not
if(num > 5 && num < 10){
    if(num == 7){
        printf("%d is an unlucky number\n", num);
    }else{
        printf("%d is a large singles digit number\n", num);
    }
    printf("%d is not a small singles digit number\n", num);
}else if (num >10){
    printf("%d is not a single digit number\n", num);
}else{
    printf("%d is not a small single digit number\n", num);
}
    return 0; 
}