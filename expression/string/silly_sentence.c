//andrea lugo, silly sentence c
#include <stdio.h>
#include <string.h>

int main(void){
char gorilla[23], mall[15], shopping[25];


printf("Tell me an animal: ");
scanf("%24s", gorilla);

printf("Tell me a place: ");
scanf("%9s", mall);

printf("Tell me an activity: ");
scanf("%19s", shopping);

printf("One day, a %s went to the %s and decided to %s all day long.\n", gorilla, mall, shopping);

return 0;
}