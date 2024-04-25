#include <stdio.h>

int ReturnPlusOne(int n) {
    return n+1;
}

int ChangePlusOne(int n) {
    n += 1;
}

int ChangePlusPointer(int *n) {
    *n += 1;
}

int main(void) {
    int number = 3;
    printf("%d\n", number);

    number = 5;
    printf("%d\n", number);

    number = ReturnPlusOne(number);
    printf("%d\n", number);

    // 함수 안의 N과 내가 넘겨준 number는 다른 값이므로 반영되지 않는다.
    ChangePlusOne(number);
    printf("%d\n", number);

    ChangePlusPointer(&number);
    printf("%d\n", number);
    return 0;
}