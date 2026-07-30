#include <stdio.h>
 
int main() {
 
  int x[10], c;
  scanf("%d", &c);
  x[0]=c;
  for(int i=1; i<=10; i++)
  {
      x[i]=2*x[i-1];
  }
      


for(int i=0; i<10; i++)
{
    printf("N[%d] = %d\n", i, x[i]);
}
    return 0;
}
