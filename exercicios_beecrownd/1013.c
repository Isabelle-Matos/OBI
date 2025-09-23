#include <stdio.h>
#include <stdlib.h>

int main(){

    int x, y, z, maior;
    scanf("%d %d %d", &x, &y, &z);
    maior = (x+y+abs(x-y))/2;
    maior = (maior+z+abs(maior -z))/2;
   
    printf("%d eh o maior\n", maior);
    

    return 0;
}
