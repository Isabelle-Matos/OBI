#include <stdio.h>
#define SENHA 2002

int main()
{
    int n;
    scanf("%d", &n);
 
    while(n!= SENHA){ 
           
        printf("Senha Invalida\n");  
        scanf("%d", &n);
   
    }
    printf("Acesso Permitido\n");
   
  
 
  
    return 0;
}
