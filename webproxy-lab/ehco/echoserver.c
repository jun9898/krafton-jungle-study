#include "../csapp.h"


void echo(int connfd);


int main(int argc, char **argv) {
    int listenfd, connfd;
    socklen_t clientlen;
    struct sockaddr_storage clientaddr;
    char client_hostname[MAXLINE], client_port[MAXLINE];

    if (argc != 2) {
        fprintf(stderr, "usage: %s <port>\n", argv[0]);
        exit(0);
    }

    listenfd = open_listenfd(argv[1]);
    while (1) {
        clientlen = sizeof(struct sockaddr_storage);
        // accept가 선언되면 listenfd 소켓을 열고 입력이 들어올때까지 프로세스를 중단하고 기다린다.
        // SA를 붙히는 이유는 clientaddr이 내 소켓의 규격과 맞지 않을 수 있으니 우선 범용 주소정보를 받아오고 형변환을 해준다.
        connfd = accept(listenfd, (SA *)&clientaddr, &clientlen);
        // 클라이언트 소켓 주소, 소켓 주소 길이, 호스트명을 저장할 버퍼, 버퍼의 최대 크기, 클라이언트의 포트를 저장할 버퍼, 버퍼의 최대 크기, 플래그 없음
        Getnameinfo((SA *) &clientaddr, clientlen, client_hostname, MAXLINE, client_port, MAXLINE, 0);
        printf("Connected to (%s, %s)\n", client_hostname, client_port);
        echo(connfd);
        Close(connfd);
    }
    exit(0);
}


void echo(int connfd) {
    size_t n;
    char buf[MAXLINE];
    rio_t rio;

    Rio_readinitb(&rio, connfd);
    while((n = Rio_readlineb(&rio, buf, MAXLINE)) != 0) {
        printf("buf = %s", buf);
        printf("server received %d bytes\n", (int)n);
        Rio_writen(connfd, buf, n);
    }
}