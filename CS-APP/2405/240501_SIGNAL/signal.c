#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <signal.h>

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

//     if ((pid = Fork()) == 0) {
//         pause();
//         printf("control should never reach here!\n");
//         exit(0);
//     }
//     kill(pid, SIGKILL);
//     exit(0);
// }

void singint_handler(int sig) {
    printf("Caught SIGINT!\n");
    exit(0);
}

int main() {
    if (signal(SIGINT, singint_handler) == SIG_ERR)
        unix_error("Signal error");
    
    pause();

    return 0;
}