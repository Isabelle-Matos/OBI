#include <stdio.h>

int main(){

    int n, count =0, x, y;
    float div;
    scanf("%d", &n);

    while(count<n){

        scanf("%d %d", &x, &y);
         count++;
        if(y==0){
            printf("divisao impossivel\n");
        }
        else if(x==0){
            div = 0.0;
            printf("%.1f\n", div);
        }
        else{
           
            div = ((float)x/y);
            printf("%.1f\n", div);
        }
    


    }

    return 0;
}
