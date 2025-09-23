#include <stdio.h>
#include <stdbool.h>

bool confere_linha(int matriz[9][9]){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            for(int k=0; k<9; k++){
                if((j!=k) && (matriz[i][j] == matriz[i][k])){
                    return false;
                    break;
                }        
            }
        }
    }
    return true;  
}
bool confere_coluna(int matriz[9][9]){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            for(int k=0; k<9; k++){
                if((j!=k) && (matriz[j][i] == matriz[k][i])){
                    return false;
                    break;
                }        
            }
        }
    }
    return true;  
}
bool confere_quadrado(int matriz[3][3]){
    int count =0;
    int vetor[9] = {1,2,3,4,5,6,7,8,9};
    for(int k=0; k<9; k++){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            if(matriz[i][j] == vetor[k]) count++;   
            } 
        }
         if(count >1) return false; 
          count = 0;    
    }

    return true;
}
bool confere_quadrado_9x9(int matriz[9][9]){
    int m[3][3];
    for(int i=0; i<9; i+=3){
        for(int j=0; j<9; j+=3){
            for(int k = 0; k<3; k++){
                for(int l=0; l<3; l++){
                    m[k][l] = matriz[k+i][l+j];
                }        
            }
               if(!confere_quadrado(m)) return false;   
       
        }
    }
    return true;
}

int main(){

    int matriz[9][9], n;
    scanf("%d", &n);
    for(int i=0; i<n; i++){ 
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            scanf("%d", &matriz[i][j]);
            }
        }
        printf("Instancia %d\n", i+1);
         if(confere_coluna(matriz) && confere_linha(matriz) && confere_quadrado_9x9(matriz)) printf("SIM\n");

        else printf("NAO\n");
        printf("\n");
        }
    


    return 0;
}
