#include <stdio.h>
#include <stdlib.h>

void func(int *arr, int num) {
    for (int i = 0; i < num; i++) {
        arr[i] += 1;
    }

}

int main(void) {
    int arr[5] = {1,2,3,4,5};
    func(arr,5);
    for (int i = 0; i < 5; i++) {
        printf("%d \n",arr[i]);
    }

    return 0;
}