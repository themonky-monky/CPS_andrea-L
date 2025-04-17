//andrea lugo, loops notes c
#include <stdio.h>

int main(void){
// 1. What is a loop? 
     // A section of code the repeats
// 2.What are the two types of loops?
    //for lops
    int x;
    for(x=0;x<10;x++){
        printf("hello\n");  
    }
    //while loops
    int i=1;
    while(i<10){
        printf("%d\n",i); 
        i++;
    }

// 3.What is iteration
    //the act of repeating
    //reference an interation as a specific time through the loop

// 4.What are lists?
      // a bunch of values in 1 variable
    
    // 8.How do you make lists in C?
      int grades[] = {97, 95, 100, 70, 94, 98, 64};
    //in the brackets we say how long the list will be, if list is set there brackets can be black
    //data type is give as whatever is in the list (all list items must be the same data type)
    //list is surrounded by curly brackets{} with commas , between each item
    printf("%d\n", grades[3]); //to print one item we put the index number in the bracket when we print
    grades[2] = 73; //update grades one at time using the indet number
    printf("%d\n", grades[2]); 
    //this tells me the number of bytes in my array(list)
    //printf("%lu", sizeof(grades));
    //how to get the size of an array(list)
    int length = sizeof(grades)/sizeof grades[0];
    printf("%d\n", length);

// 9.How do you make for loops in C?
    //iterators should be x or i 
    int t;
    //in parent 1. startring point 2. go util point 3. what we count by
    for(t=0;t<5;t++){
        printf("%d\n", t);  
    }
    int l;
    for(l=0;l<length;l++){
        printf("%d\n", grades[l]);
    }

    // 10.How do you make while loops in C?
// use iterator to set start point
int iterator = 100;
//while line sets the stop point/ how long it goes

while(iterator <=0){

    printf("%d\n", iterator);
    //set what I count by
    iterator -=10;

}

char movies[][20] ={"Cinderella", "the smerf movie", "transformers", "cars", "Up", "1984"};
int mlength = sizeof(movies)/sizeof(movies[0]);
int m=0; 
while(m<mlength){; 
    printf("%s\n", movies[m]);
    m++; 
}
    return 0; 

}