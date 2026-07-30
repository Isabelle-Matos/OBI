#include <stdio.h>
#include <string.h>


void contador(char *string, char *substring){
    int count = 0;
    char *indice;//ponteiro de char pq vai receber como atributo o valor de p
    char *p = strstr(string, substring);
    while(p!=NULL){
    count++;
    indice = p;// p aponta para o primeiro caractere da substring encontrado na string
    p+= strlen(substring);
    p = strstr(p, substring);/*p == posicao do primeiro char depois da substring,
                                se a string = 123412 e a sub = 12, p = 34
                                */ 
    
    }
   if(count == 0){
    printf("Nao existe subsequencia\n");
   }
   else if(count !=0){
    printf("Qtd.Subsequencias: %d\n", count);
    printf("Pos: %d\n", indice - string + 1 );/*indice vai ser igual a ultima posicao do caractere da 
                                                substring encontrado na string, e como um vetor e um ponteiro que 
                                                aponta pra primeira posicao, string - indice +1 = ultima posicao encontrada
                                                */
    }
}
int main(){
    int count = 0, caso = 1;
    char substring[10], string[32];
    scanf("%s %s", substring, string);
  
    while(!feof(stdin)){
        printf("Caso #%d:\n", caso);
        contador(string, substring);
        printf("\n");
        caso++;
        scanf("%s %s",substring, string);
      
    }
    
    
    return 0;
}
