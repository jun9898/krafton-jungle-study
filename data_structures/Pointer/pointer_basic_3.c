#include <stdio.h>
void mul(int *n) {
    *n = *n * 2;
}

int main(void) {
    int a;
    scanf("%d", &a);

    mul(&a);
    printf("%d \n", a);
    return 0;
}