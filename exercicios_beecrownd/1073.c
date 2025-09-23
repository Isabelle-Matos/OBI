#include <stdio.h>

int main() {

	int n;

	do {
		scanf("%d", &n);
	} while (n <= 5 || n >= 2000); 

	for (int i = 2; i <= n ; i+=2) {
		printf("%d^%d = %d\n", i ,2 ,i*i);
	}

	return 0;
}
