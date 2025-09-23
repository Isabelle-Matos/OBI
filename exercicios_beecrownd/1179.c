#include<stdio.h>


int main(){

    int par[5], impar[5], n, cont1 =0, cont2 =0;

    for(int i=0; i<15; i++){
        scanf("%d", &n);
      if(n%2==0){
        par[cont1] = n;
        cont1++;
        if(cont1 == 5){
            for(int i=0; i<5; i++){
                printf("par[%d] = %d\n", i, par[i]);
            }
            cont1 = 0;
        }
      }
      else if(n%2!=0){
        impar[cont2] = n;
        cont2++;
        if(cont2 == 5){
            for(int i=0; i<5; i++){
                printf("impar[%d] = %d\n", i, impar[i]);
            }
            cont2 = 0;
        }
      }
    }

    for(int i=0; i<cont2; i++){
            printf("impar[%d] = %d\n", i, impar[i]);
        }

    for(int i=0; i<cont1; i++){
            printf("par[%d] = %d\n", i, par[i]);
        }
       
 



    return 0;
}
