#include <stdio.h>

int main(void) {
    // 포인터의 연산
    int *ptr1 = 0x0010;
    double *ptr2 = 0x0010;

    // int 자료형의 포인터는 4씩 증가
    printf("%p %p \n", ptr1+1, ptr1+2);
    // double 자료형의 포인터는 8씩 증가
    printf("%p %p \n", ptr2+1, ptr2+2);

    printf("%p %p \n", ptr1, ptr2);
    ptr1++;
    ptr2++;
    printf("%p %p \n", ptr1, ptr2);
}
