#include <stdio.h>
 
int main() {
 
    int x, div1=0, div2=0, div3=0, div4=0, div5=0, div6=0, div7=0;
    scanf("%d", &x);
    printf("%d\n", x);
      if(x>=100){
         div1 = x/100;
         x = x%100;
      }
      if(x<100 && x>=50){
         div2= x/50;
         x = x%50;

      }
      if(x<50 && x>=20){
         div3= x/20;
         x=x%20;
      }
      if(x<20 && x>=10){
         div4=x/10;
         x= x%10;

      }
      if(x<10 && x>=5){
         div5=x/5;
         x=x%5;

      }
      if(x<5 &&x>=2){
         div6= x/2;
         x=x%2;
      }
      if(x<2 && x>=1){
         div7=x/1;
         x=x%1;
    }
      printf("%d nota(s) de R$ 100,00\n", div1 );
      printf("%d nota(s) de R$ 50,00\n", div2 );
      printf("%d nota(s) de R$ 20,00\n", div3 );
      printf("%d nota(s) de R$ 10,00\n", div4 );
      printf("%d nota(s) de R$ 5,00\n", div5 );
      printf("%d nota(s) de R$ 2,00\n", div6 );
      printf("%d nota(s) de R$ 1,00\n", div7 );
    
  
      

 
    return 0;
}
