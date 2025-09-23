#include <stdio.h>

int main(){
    
    int a, in =0, out=0;
    scanf("%d", &a);
    int n[a];

    for(int i =0; i<a; i++){
        scanf("%d", &n[i]);
        if(n[i]>=10 && n[i]<=20){
            in++;
        }
        else if(n[i]<10 || n[i]>20){
            out++;
        }
    }
    printf("%d in\n", in);
    printf("%d out\n", out);
    
   
       
    

    return 0;
}
