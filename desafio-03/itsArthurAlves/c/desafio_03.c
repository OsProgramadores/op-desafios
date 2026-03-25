#include <stdio.h>

int inverter(int y){
  int z = 0;
  while(y>0){
   z = (z*10) + (y%10);
   y = (y/10);
  };
  return(z);
}
void main(){
  int initial, final, i, z;
  printf("Type the initial number: ");
  scanf("%d", &initial);
  printf("\nType the final number: ");
  scanf("%d", &final);
  if(initial<final){
    for (i=initial; i<=final; i++){
      z = inverter(i);
      if(z == i)
        printf("This is: %d.\n", z);
    };
  }else
    printf("Invalid interval.\n");
}
