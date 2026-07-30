#include<stdio.h>
float salario(float s){
    float desc, sal, faixa1=0, faixa2=0, faixa3=0;
    if(s>2000.00 && s<=3000.00){
        faixa1 = s-2000.0;
        desc = faixa1*0.08;
    }
    else if(s>3000.00 && s<=4500.00){
        faixa1 = 1000.0;
        faixa2 = s - 3000.0;
        desc = (faixa2*0.18)+(faixa1*0.08);
    }
    else{
        faixa3= s-4500.0;
        faixa2= 1500.0;
        faixa1 = 1000.0;
        desc = (faixa3*0.28) + (faixa2*0.18) + (faixa1*0.08);
    }

    return desc;

}

int main(){

    float s;
    scanf("%f", &s);
    if (s>0 && s<=2000.00){printf("Isento\n");}
    else{
        printf("R$ %.2f\n", salario(s));
        }


    return 0;
}
