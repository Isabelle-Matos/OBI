#include <stdio.h>


int main(){

    int A[20] = {0};
    int aux = 0;

    for(int i=0; i<20; i++){
        scanf("%d", &A[i]);
      
    }

    for(int i=0; i<10; i++){
   

        aux = A[i];
        A[i] = A[19-i];
        A[19-i] = aux;
      
     
        }
       
    for(int i=0; i<20; i++){
         printf("N[%d] = %d\n", i, A[i]);
    }




    return 0;
}
