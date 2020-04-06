#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
void structure(int actualnumber2){
  int  x, order = 1, indicator;
  bool io = false;
  for (actualnumber2=1; actualnumber2<=10000; actualnumber2++){ 
    for (x = 1; x<=actualnumber2; x++){
      if (actualnumber2%x==0)
        indicator++;
    }
    if (indicator==2)
        io = true;
    if (io==true){
      printf("The %dº number is this: %d.\n", order, actualnumber2);
      order++;
    }
    io = false;
    indicator = 0;
  };
};
void main (){
  int actualnumber;
  structure(actualnumber);
}