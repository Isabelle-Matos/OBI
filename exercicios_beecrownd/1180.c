#include <stdio.h>



int main(){

    int n, pos=0, menor=0;
    scanf("%d", &n);
    int vet[n];

    for(int i=0; i<n; i++){
        scanf("%d", &vet[i]);
       menor = vet[n-1];
    }

    for(int i=0; i<n; i++){
        if(menor > vet[i]){
            menor = vet[i];
            pos = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", pos);


    return 0;
}
