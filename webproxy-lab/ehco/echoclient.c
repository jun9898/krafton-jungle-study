#include "../csapp.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int clientfd;
    char *host, *port, buf[MAXLINE];
    char tmp[MAXLINE];
    rio_t rio;

    if (argc != 3) {
        fprintf(stderr, "usage: %s <host> <port>\n", argv[0]);
        exit(0);
    }

    host = argv[1];
    port = argv[2];

    // host와 conected된 clientfd
    clientfd = open_clientfd(host, port);
    rio_readinitb(&rio, clientfd);

    while(Fgets(buf, MAXLINE, stdin) != NULL) {
        rio_writen(clientfd, buf, strlen(buf));
        rio_readlineb(&rio, tmp, MAXLINE);

        printf("====================\n");
        Fputs(buf, stdout);
        Fputs(tmp, stdout);
        printf("====================\n");
    }
    Close(clientfd);
    exit(0);
    
}