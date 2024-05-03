#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>

#define MAXLINE 1024

int main(int argc, char *argv[]) {
    struct addrinfo hints, *listp, *p;
    int rc, flag;
    char buf[MAXLINE];

    if (argc != 2) {
        fprintf(stderr, "Usage: %s domain name\n", argv[0]);
        exit(0);
    }

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    if ((rc = getaddrinfo(argv[1], NULL, &hints, &listp)) != 0) {
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(rc));
        exit(0);
    }

    printf("IP addresses for %s:\n\n", argv[1]);

    for (p = listp; p != NULL; p = p->ai_next) {
        flag = getnameinfo(p->ai_addr, p->ai_addrlen, buf, sizeof(buf), NULL, 0, NI_NUMERICHOST);
        if (flag != 0) {
            fprintf(stderr, "getnameinfo error: %s\n", gai_strerror(flag));
            continue;
        }
        printf("%s\n", buf);
    }

    freeaddrinfo(listp);
    return 0;
}