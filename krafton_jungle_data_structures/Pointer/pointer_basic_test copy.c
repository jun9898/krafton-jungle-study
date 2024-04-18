#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *arr = (int *) malloc(5 * sizeof(int));
    for (int i = 0; i<5; i++) {
        arr[i] = i*i;
        printf("%d \n", arr[i]);
    }
    printf("%d \n", arr[3]);
    free(arr);
    return 0;
}