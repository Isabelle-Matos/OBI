#include <stdio.h>


int main(){

    int x, y;
    scanf("%d %d", &x, &y);

    do{
        if (x==0 || y == 0){
            break;
        }
       else if(x>0 && y>0){
            printf("primeiro\n");
        }
        else if(x>0 && y<0){
            printf("quarto\n");
        }
        else if(x<0 && y>0){
            printf("segundo\n");
        }
        else if(x<0 && y<0){
            printf("terceiro\n");
        }
        scanf("%d %d", &x, &y);

    }while (1);
    
    

    return 0;
}
