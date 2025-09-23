#include <stdio.h>

int main(){

    float matriz[12][12], soma =0.0;
    char resposta;
    int k =0;
    scanf("%c", &resposta);

    for(int i=0; i<12; i++){
        for(int j=0; j<12; j++){
            scanf("%f", &matriz[i][j]);
        }
    }

    for(int i=0; i<12; i++){
        for(int j=0; j<11-i; j++){
                soma+=matriz[i][j];
        }
    }
    if(resposta == 'S')
    printf("%.1f\n", soma);
    else if(resposta == 'M')
    printf("%.1f\n", soma/66);
    return 0;
}
