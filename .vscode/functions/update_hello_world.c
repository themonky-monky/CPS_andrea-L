//Andrea lugo, update_hello_world.c
#include <stdio.h>

void info(char name[]){
    printf("hello, %s!\n", name);

}
int main(void){
    info("andrea");
    info("lucas");
    info("carlos");
    info("alejandro");
    info("rocio");
    return 0; 
}