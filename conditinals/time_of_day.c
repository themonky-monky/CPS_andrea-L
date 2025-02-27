//andrea lugo, time of day c
#include <stdio.h>
#include <time.h>

int main(void){
    //time since jan 1, 1970
    time_t seconds;

    seconds = time(NULL);
    printf("seconds since januari 1, 1970 = %ld\n", seconds);

    //current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("current time and date is %s", asctime(timeinfo));

//curent hour
time_t now = time(NULL);
struct tm *tm_struct = localtime(&now);
int hour = tm_struct->tm_hour;
printf("%d\n", hour);

if (hour <12){
    printf("good morning\n");
}else if (hour <19 ){
    printf("good afternoon\n");
}else if (hour <24){
    printf("good evening\n");
}
return 0; 

}