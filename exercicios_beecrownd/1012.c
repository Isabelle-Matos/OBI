#include<stdio.h>
#define pi 3.14159

int main(){

    double x, y, z, area_tri = 0, area_cir = 0, area_trap = 0, area_quad = 0, area_ret = 0;
    scanf("%lf %lf %lf", &x, &y, &z);
    area_tri = (x*z)/2;
    area_cir = pi*(z*z);
    area_trap = ((x+y)*z)/2;
    area_quad = y*y;
    area_ret = x*y;
    printf("TRIANGULO: %.3lf\n", area_tri);
    printf("CIRCULO: %.3lf\n", area_cir);
    printf("TRAPEZIO: %.3lf\n", area_trap);
    printf("QUADRADO: %.3lf\n", area_quad);
    printf("RETANGULO: %.3lf\n", area_ret);







    return 0;
}
