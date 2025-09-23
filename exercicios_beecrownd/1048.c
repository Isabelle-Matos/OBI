#include <stdio.h>
 
int main() {
    float x;
    scanf("%f", &x);
    if(x >= 0 && x <= 400.00){
        printf("Novo salario: %.2f\n", x*1.15);
        printf("Reajuste ganho: %.2f\n", (x*1.15)-x);
        printf("Em percentual: 15 %%\n");
    }
    else if(x >= 400.01 && x <= 800.00){
        printf("Novo salario: %.2f\n", x*1.12);
        printf("Reajuste ganho: %.2f\n", (x*1.12)-x);
        printf("Em percentual: 12 %%\n");
    }
    else if(x >= 800.01 && x <= 1200.00){
        printf("Novo salario: %.2f\n", x*1.10);
        printf("Reajuste ganho: %.2f\n", (x*1.10)-x);
        printf("Em percentual: 10 %%\n");
    }
    else if(x >= 1200.01 && x <= 2000.00){
        printf("Novo salario: %.2f\n", x*1.07);
        printf("Reajuste ganho: %.2f\n", (x*1.07)-x);
        printf("Em percentual: 7 %%\n");
    }
    else if(x > 2000.00){
        printf("Novo salario: %.2f\n", x*1.04);
        printf("Reajuste ganho: %.2f\n", (x*1.04)-x);
        printf("Em percentual: 4 %%\n");
    }
 
    return 0;
}
