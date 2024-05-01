#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

void unix_error(char *msg) {
    fprintf(stderr, "%s : %s\n", msg, strerror(errno));
    exit(0);
}

pid_t Fork(void) {
    pid_t pid;
    if ((pid = fork()) < 0)                     // fork 함수는 한번 호출하지만 총 2개의 반환값 가진다.
        unix_error("Fork error");
    return pid;
}

// int main() {
//     pid_t pid;
//     int x = 1;

//     pid = Fork();
//     if (pid == 0) {                             // 자식 프로세스는 PID가 0임으로 조건에 걸린다.
//         printf("child : x=%d \n", ++x);
//         printf("pid = %d\n", pid);
//         exit(0);
//     }

//     printf("parent : x=%d\n", --x);             // 부모 프로세스는 자식의 PID를 가지고 있기 때문에 조건에 걸리지 않는다.
//     printf("pid = %d\n", pid);
//     exit(0);
// }

int main() {
    int a = 9;

    if (Fork() == 0) {
        printf("p1 : a = %d \n", a--);
    }
    printf("p2 : a = %d \n", a++);
    exit(0);
}