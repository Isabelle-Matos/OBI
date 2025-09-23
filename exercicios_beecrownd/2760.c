#include <stdio.h>
#include <string.h>



int main(){
    
    char aux;
    char stringA[3][101], stringD[101];
    for(int i=0; i<3; i++){
        fgets(stringA[i], 101, stdin);
      
    }
    for(int i=0; i<3; i++){
        int j = strlen(stringA[i]);
        stringA[i][j-1] = '\0';
    }
   
    printf("%s%s%s\n", stringA[0], stringA[1], stringA[2]);
    printf("%s%s%s\n", stringA[1], stringA[2], stringA[0]);
    printf("%s%s%s\n", stringA[2], stringA[0], stringA[1]);
    printf("%.10s%.10s%.10s\n", stringA[0], stringA[1], stringA[2]);

   
    
  
    return 0;
}
