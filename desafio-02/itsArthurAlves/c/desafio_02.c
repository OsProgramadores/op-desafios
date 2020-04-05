#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


void structure(int actualnumber2){
  int  indicator=1;
  bool order = false;
  for (actualnumber2=1; actualnumber2<=10000; actualnumber2++){ 
   if (actualnumber2%2 != 0){
    order = true;
   };
   if(order == true){
    printf ("The %dº number = %d\n", indicator, actualnumber2);
    indicator++;
   };
   order = false;
  };
};
 
void main (){
  int actualnumber;
  structure(actualnumber);

}