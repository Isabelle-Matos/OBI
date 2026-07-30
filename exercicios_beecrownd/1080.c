#include <stdio.h>


int main()
{
    int a[100], maior=0, posi;
    for(int i = 1; i<=100; i++){
        scanf("%d", &a[i]);
    }
 
  for(int i=1; i<=100; i++){
    if(maior<a[i]){
        maior = a[i];
        posi = i;
    }
  }
  printf("%d\n", maior);
  printf("%d\n", posi);
 
  
    return 0;
}
