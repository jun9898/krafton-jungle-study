#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;

    // 5개의 int 형 변수에 대한 메모리 할당
    ptr = (int *)malloc(5 * sizeof(int));
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // 메모리 블록의 크기를 10개의 int 형 변수로 변경
    ptr = (int *)realloc(ptr, 10 * sizeof(int));
    if (ptr == NULL) {
        printf("Memory reallocation failed\n");
        return 1;
    }

    // 메모리 해제
    free(ptr);

    return 0;
}