#include <stdio.h>
 
int main() {
 int c,q;
 float total;
 scanf("%d %d" , &c,&q);
 
	if(c == 1)
	{
		total = 4.00*q;	
	}else
	if(c == 2){
		total = 4.50*q;
	}else 
	if(c == 3){
		total = 5.00*q;
	}else
	if(c == 4)
	{
		total = 2.00*q;
	}else
	if(c == 5)
	{
		total = 1.50*q;
	}
	
	printf("Total: R$ %.2f\n",total);
}
