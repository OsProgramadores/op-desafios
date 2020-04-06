#include <stdio.h>
#include <stdlib.h>
void primos(){
  int  actualnumber, x, order = 1, sinalization;
  for (actualnumber=2; actualnumber<=10000; actualnumber++){
    for (x = 2; x<=actualnumber; x++)
      if (actualnumber%x==0)
        sinalization++;
    if (sinalization == 1){
      printf("The %dº number is this: %d.\n", order, actualnumber);
      order++;
    };
    sinalization = 0;
  };
};
void main (){
  primos();
}