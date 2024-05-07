#include <stdio.h>
#include "csapp.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

/* You won't lose style points for including this long line in your code */
static const char *user_agent_hdr ="User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 Firefox/10.0.3\r\n";

void doit(int clientfd);
void clienterror(int fd, char *cause, char *errnum, char *shortmsg, char *longmsg);
void parse_uri(char *uri, char *hostname, char *port, char *path);


int main(int argc, char **argv) {
    int listenfd, clientfd;                                                               // 요청을 보내는 클라이언트의 fd를 얻을거임
    char hostname[MAXLINE], port[MAXLINE];
    socklen_t clientlen;
    struct sockaddr_storage clientaddr;

    /* Check command line args */
    if (argc != 2) {
        fprintf(stderr, "usage: %s <port>\n", argv[0]);
        exit(1);
    }

    listenfd = Open_listenfd(argv[1]);                                                    // 프록시 listenfd 열어주기

    while (1) {
        clientlen = sizeof(clientaddr);
        clientfd = Accept(listenfd, (SA *)&clientaddr, &clientlen); 
        Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE, 0);
        printf("Accepted connection from (%s, %s)\n", hostname, port);
        doit(clientfd);   
        Close(clientfd);  
    }
}


void doit(int clientfd) { 
    int serverfd;                                                                       // End server와의 소켓도 연결해야 하기 때문에 fd를 저장할 int 자료형 초기화
    char request_buf[MAXLINE], response_buf[MAX_OBJECT_SIZE];                           // client의 요청과 server의 response를 저장할 버퍼 선언                
    char path[MAXLINE], method[MAXLINE], uri[MAXLINE];                 
    char hostname[MAXLINE], port[MAXLINE];                                           
    rio_t request_rio, response_rio;                                                    // request rio, response rio 설정

    Rio_readinitb(&request_rio, clientfd);                                              // client의 request를 전달할 rio 세팅
    Rio_readlineb(&request_rio, request_buf, MAXLINE);                                  // 읽어서 buf에 저장할거임
    printf("Request headers : %s", request_buf);

    sscanf(request_buf, "%s %s", method, uri);                                          // 나눠서 각각 검사할거임

    if (strcasecmp(method, "GET") && strcasecmp(method, "HEAD")) {                      // GET과 일치하면 0 다르면 1을 리턴함으로 다르면 501 error코드를 발생시킨다
        clienterror(clientfd, method, "501", "Not implemented", "Tiny does not implement this method");
        return;
    }
    parse_uri(uri, hostname, port, path);                                               // uri에서 호스트명, 포트, 경로를 파싱

    sprintf(request_buf, "%s /%s %s\r\n", method, path, "HTTP/1.0");                    // 요청 재구성
    sprintf(request_buf, "%sConnection: close\r\n", request_buf);                       // 재수성된 요청 바탕으로 다시 헤더 작성
    sprintf(request_buf, "%sProxy-Connection: close\r\n", request_buf); 
    sprintf(request_buf, "%s%s\r\n", request_buf, user_agent_hdr); 

    if (strcasecmp(method, "GET") && strcasecmp(method, "HEAD")) {
        clienterror(clientfd, method, "501", "Not Implemented", "Proxy does not implement this method");
        return;
    }

    serverfd = Open_clientfd(hostname, port);                                           // end server 와의 소켓 연결
    Rio_writen(serverfd, request_buf, strlen(request_buf));                             // 서버에 요청!

    ssize_t n;
    Rio_readinitb(&response_rio, serverfd);                                             // 서버의 요청을 받을 response_rio 세팅
    while ((n = Rio_readlineb(&response_rio, response_buf, MAX_OBJECT_SIZE)) > 0) {     // response_rio를 통해 버퍼에 응답 저장
        Rio_writen(clientfd, response_buf, n);
        if (!strcmp(response_buf, "\r\n"))                                              // 만약 헤더가 아니면 break
            break;
    }

    while ((n = Rio_readlineb(&response_rio, response_buf, MAX_OBJECT_SIZE)) > 0) {     // response_rio를 통해 버퍼에 응답 저장
        Rio_writen(clientfd, response_buf, n);                                          // body 나머지 전송
    }
    Close(serverfd);
}



void clienterror(int fd, char *cause, char *errnum, char *shortmsg, char *longmsg) {
    char buf[MAXLINE], body[MAXBUF];
    sprintf(body, "<html><title>Tiny Error</title>");
    sprintf(body, "%s<body bgcolor=""ffffff"">\r\n", body);
    sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
    sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
    sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n", body);
    
    sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-type: text/html\r\n");
    Rio_writen(fd, buf, strlen(buf));
    sprintf(buf, "Content-length: %d\r\n\r\n", (int) strlen(body));
    Rio_writen(fd, buf, strlen(buf));
    Rio_writen(fd, body, strlen(body));
}


void parse_uri(char *uri, char *hostname, char *port, char *path) {                         // 호스트명, 포트, 경로로 파싱

    char *hostname_ptr = strstr(uri, "//") != NULL ? strstr(uri, "//") + 2 : uri + 1;       // // 기호가 시작되는 부분 기준 +2를 해야 hostname으로 접근 가능
    char *port_ptr = strstr(hostname_ptr, ":");                                             // port의 시작부분을 가르키는 포인터   
    char *path_ptr = strstr(hostname_ptr, "/");                                             // 경로를 가르키는 포인터    

    if (path_ptr > 0) {                                                                     // 경로가 존재한다면
        *path_ptr = '\0';                                                                   // 문자열 끊어주기
        strcpy(path, path_ptr+1);                                                           // 경로를 path 버퍼에 복사
    }

    if (port_ptr > 0) {
        *port_ptr = '\0'; 
        strcpy(port, port_ptr + 1); 
    }

    strcpy(hostname, hostname_ptr);
    printf("host : %s, port : %s, path : %s\n",hostname, port, path);
}


void read_requesthdrs(rio_t *rp) {
    char buf[MAXLINE];

    // HTTP 헤더를 읽어들임
    Rio_readlineb(rp, buf, MAXLINE);
    while(strcmp(buf, "\r\n")) { // 빈 줄이 나올 때까지 반복
        Rio_readlineb(rp, buf, MAXLINE);
        printf("%s", buf); // 헤더를 화면에 출력하거나 다른 작업을 수행할 수 있음
    }
    return;
}