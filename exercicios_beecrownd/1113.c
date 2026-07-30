#include <stdio.h>

int verifica(int *x, int *y){
    if(*x>*y) return 0;
    else return 1;
}

int main(){

    int x, y;
    scanf("%d %d", &x, &y);

    while(x != y){
 
        if(verifica(&x, &y) == 1){
            printf("Crescente\n");
        }
        else{
            printf("Decrescente\n");
        }
        scanf("%d %d", &x, &y);
    }


    return 0;
}
