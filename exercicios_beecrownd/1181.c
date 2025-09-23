#include <stdio.h>



int main(){

    int n;
    double soma = 0.0, matriz[12][12];
    char resposta[2];
    scanf("%d", &n);
    scanf("%s", resposta);
    

     for(int i=0; i<12; i++){
        for(int j=0; j<12; j++){
            scanf("%lf", &matriz[i][j]);
            if(i==n){
                soma+= matriz[i][j];
            }
        }
     }

    

    if(resposta[0]=='S'){
        printf("%.1lf\n", soma);
    }
    else if(resposta[0]=='M'){
        printf("%.1lf\n", soma/12.0);
    }


    return 0;
}
