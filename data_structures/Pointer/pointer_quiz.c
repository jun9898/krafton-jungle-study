#include <stdio.h>

// 1, 2
void swap(int *px, int *py) {
    printf("========================\n");
    printf("px = %p py = %p \n", px, py);
    printf("*px = %d *py = %d \n", *px, *py);
    *px = *px - *py;
    *py = *px + *py;
    *px = *py - *px;
    printf("px = %p py = %p \n", px, py);
    printf("*px = %d *py = %d \n", *px, *py);
    printf("========================\n");

}

int main(void) {
    int i = 1;
    int j = 2;
    swap(&i, &j);

    printf("i = %d j = %d \n",i,j);
}