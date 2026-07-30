#include <stdio.h>
#include <string.h>

int main() {
   
    int n;
    while(scanf("%d", &n) != EOF){
        getchar();
        for(int i = 0; i < n; i++){
            int espaco = 0;
            int qtd_pontos = 0;
            char pontos[51];
            fgets(pontos, 51, stdin);
            pontos[strlen(pontos) - 1] = '\0';

            for(int i = 0; pontos[i] != '\0'; i++){
                if(pontos[i] == ' ') espaco++;
            }

             for(int i = 0; pontos[i] != '\0'; i++){
                if(pontos[i] == ' ') break;
                qtd_pontos++;
            }

            int c = 96 + (espaco * 3) + qtd_pontos;

            printf("%c\n", c);
        }
    }

    return 0;
}
