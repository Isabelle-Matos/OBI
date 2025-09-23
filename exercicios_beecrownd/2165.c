#include <stdio.h>
#include <string.h>
int main(){
      char T[501];
      fgets(T,501,stdin);
      int tamanho = strlen(T)-1;
      if(tamanho>140){
            printf("MUTE\n");
      }else{
            printf("TWEET\n");
      }
      return 0;
}
