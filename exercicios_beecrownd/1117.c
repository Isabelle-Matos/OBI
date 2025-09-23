#include <stdio.h>


int main(){

    float x, count = 0, media=0;
 

    while(count != 2){
       scanf("%f", &x);
       if(x<0 || x>10){
            printf("nota invalida\n");
        }
        
         else if(x>= 0 && x<=10){
            media+= x;
            count++;
        }

        
        
        if(count == 2){
            printf("media = %.2f\n", media/2);
        }
     
       
    }




    return 0;
}
