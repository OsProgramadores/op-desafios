#include <stdio.h>

bool isPalindrome(int number){
	int pal=0;
	int original=number;
	while(number>0){
		int LastDigit=number%10;
		pal = (pal*10)+LastDigit;
		number= number/10;
	}
	return original==pal ? true:false;
}
int main(){
	int init,fin;

	printf(".:Enter a range (positive integer):.\n");
	printf("Start: ");
	scanf("%d",&init);
	printf("End: ");
	scanf("%d",&fin);

	while(init<fin){
		if(isPalindrome(init))
			printf("%d\n",init);
		init++;
	}
}
