#include <stdio.h>


int main()
{
    int n, a, b, count =0, soma =0;
    scanf("%d", &n);
    count++;
    while(count<=n){
        scanf("%d %d", &a, &b);
        if(a>b){
            for(int i=b+1; i<a; i++){
                if(i%2!=0){
                    soma+= i;
                }
            }
        }
        else if(b>a){
            for(int i=a+1; i<b; i++){
                if(i%2!=0){
                    soma+= i;
                }
        }   
    }
     printf("%d\n", soma);
     soma = 0;
     count++;
    
    }

   
  
 
  
    return 0;
}
