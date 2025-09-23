#include <stdio.h>

void estado(int i){

    if(i==61){
       printf("Brasilia\n");
    }
    else if(i==71){
        printf("Salvador\n");
    }
    else if(i==11){
        printf("Sao Paulo\n");
    }
    else if(i==21){
        printf("Rio de Janeiro\n");
    }
    else if(i==32){
       printf("Juiz de Fora\n");
    }
    else if(i==19){
        printf("Campinas\n");
    }
    else if(i==27){
        printf("Vitoria\n");
    }
    else if(i==31){
       printf("Belo Horizonte\n");
    }
    else{
        printf("DDD nao cadastrado\n");
    }
   
}

int main()
{
    int a;
    scanf("%d", &a);
    estado(a);
    
    
    return 0;
}
