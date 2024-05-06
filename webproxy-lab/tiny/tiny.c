/* $begin tinymain */
/*
 * tiny.c - A simple, iterative HTTP/1.0 Web server that uses the
 *     GET method to serve static and dynamic content.
 *
 * Updated 11/2019 droh
 *   - Fixed sprintf() aliasing issue in serve_static(), and clienterror().
 */
#include "csapp.h"

void echo(int connfd);
void doit(int fd);
void read_requesthdrs(rio_t *rp);
int parse_uri(char *uri, char *filename, char *cgiargs);
void serve_static(int fd, char *filename, int filesize, char *method);
void get_filetype(char *filename, char *filetype);
void serve_dynamic(int fd, char *filename, char *cgiargs);
void clienterror(int fd, char *cause, char *errnum, char *shortmsg,
                 char *longmsg);

int main(int argc, char **argv) {
  int listenfd, connfd;
  char hostname[MAXLINE], port[MAXLINE];
  socklen_t clientlen;
  struct sockaddr_storage clientaddr;

  /* Check command line args */
  if (argc != 2) {
    fprintf(stderr, "usage: %s <port>\n", argv[0]);
    exit(1);
  }

  listenfd = Open_listenfd(argv[1]);
  while (1) {
    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr,
                    &clientlen);  // line:netp:tiny:accept
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE, 0);
    printf("Accepted connection from (%s, %s)\n", hostname, port);
    doit(connfd);   // line:netp:tiny:doit
    // echo(connfd);
    Close(connfd);  // line:netp:tiny:close
  }
}


void doit(int fd) { 
    int is_static;
    struct stat sbuf;                                                                   // stat 구조체는 파일의 상태 정보를 저장할 구조체이다.
    char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];                 
    char filename[MAXLINE], cgiargs[MAXLINE];                                           // 각 컨텐츠를 저장할 버퍼 선언. cgiargs = CGI 프로그램에 전달한 인수를 저장할 버퍼
    rio_t rio;

    Rio_readinitb(&rio, fd);                                                            // 요청받은 FD를 읽을거임  
    Rio_readlineb(&rio, buf, MAXLINE);                                                  // 읽어서 buf에 저장할거임
    printf("Request headers : %s", buf);
    sscanf(buf, "%s %s %s", method, uri, version);                                      // 나눠서 각각 검사할거임

    if (strcasecmp(method, "GET") && strcasecmp(method, "HEAD")) {                      // GET과 일치하면 0 다르면 1을 리턴함으로 다르면 501 error코드를 발생시킨다
        clienterror(fd, method, "501", "Not implemented", "Tiny does not implement this method");
        return;
    }

    read_requesthdrs(&rio);                                                             // GET요청 외의 다른 요청을 무시한다. 나중에 함수를 작성하고 다시 확인해보자

    is_static = parse_uri(uri, filename, cgiargs);                                      // 동적, 정적 컨텐츠를 구별한다. 나중에 함수를 작성하고 다시 확인해보자

    if (stat(filename, &sbuf) < 0) {                                                    // filename은 파일의 경로, &sbuf는 상태 정보를 저장할 구조체의 포인터
        clienterror(fd, method, "404", "Not found", "Tiny couldn't find this file");
        return;
    }

    if (is_static) {                                                                    // S_ISREG는 파일의 모드를 검사하여 일반 파일인지 확인한다.
        if (!(S_ISREG(sbuf.st_mode)) || !(S_IRUSR & sbuf.st_mode))  {                   // S_IRUSR은 사용자에게 읽기 권한이 있는지 확인한다. 즉 파일의 모드와 권환을 체크하는 코드
            clienterror(fd, method, "403", "Forbidden", "Tiny couldn't read the file");
            return;
        }
        serve_static(fd, filename, sbuf.st_size, method);                                       // 클라이언트에게 정적 컨텐츠 제공
    }
    else {                                                                              // S_ISREG는 파일이 일반 파일인지 확인한다.
        if (!(S_ISREG(sbuf.st_mode)) || !(S_IXUSR & sbuf.st_mode))  {                   // S_IXUSR은 사용자(Owner)에게 실행 권한이 있는지 확인한다. 
            clienterror(fd, method, "403", "Forbidden", "Tiny couldn't run the CGI program");
            return;
        }
        serve_dynamic(fd, filename, cgiargs);
    }
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



void read_requesthdrs(rio_t *rp) {
    char buf[MAXLINE];

    Rio_readlineb(rp, buf, MAXLINE);
    while (strcmp(buf, "\r\n")) {
        Rio_readlineb(rp, buf, MAXLINE);
        printf("%s", buf);
    }
    return;
}


int parse_uri(char *uri, char *filename, char *cgiargs) {

    char *ptr;

    if (!strstr(uri, "cgi-bin")) {                                                      // 특정 문자열을 찾는 함수임
        strcpy(cgiargs, "");                                                            // 정적이니깐 관련 인자 다 날리기
        strcpy(filename, ".");                                                          // 상대 경로로 변경해주는 과정
        strcat(filename, uri);                                                          // 상대 경로로 변경해주는 과정
        if(uri[strlen(uri)-1] == '/')
            strcat(filename, "home.html");                                              // index파일로 이동
        return 1;
    } else {
        ptr = index(uri, '?');                                                          // parameter 추출
        if (ptr) {
            strcpy(cgiargs, ptr+1);
            *ptr = '\0';
        } 
        else 
            strcpy(cgiargs, "");                                                        // parameter가 없으면 그냥 날리기
        strcpy(filename, ".");
        strcat(filename, uri);
        return 0;
    }
}

void serve_static(int fd, char *filename, int filesize, char *method) {
    int srcfd;
    char * srcp, filetype[MAXLINE], buf[MAXBUF];

    get_filetype(filename, filetype);                                                   // 헤더 작성 후 client에게 전송
    sprintf(buf, "HTTP/1.0 200 OK\r\n");
    sprintf(buf, "%s Server : Tiny Web Server\r\n", buf);
    sprintf(buf, "%s Connection : close\r\n", buf);
    sprintf(buf, "%s Content-length : %d\r\n", buf, filesize);
    sprintf(buf, "%s Content-type : %s\r\n\r\n", buf, filetype);
    Rio_writen(fd, buf, strlen(buf));
    printf("Response headers : \n");
    printf("%s", buf);

    if (strcasecmp(method, "GET") == 0) {
        srcfd = Open(filename, O_RDONLY, 0);                                                // 정적 파일을 열고 메모리 할당한 뒤 전송하고 free하기
        // 숙제문제 11.9
        srcp = Mmap(0, filesize, PROT_READ, MAP_PRIVATE, srcfd, 0);
        // srcp = (char *) malloc(filesize);
        // Rio_readn(srcfd, srcp, filesize);
        Close(srcfd);
        Rio_writen(fd, srcp, filesize);
        Munmap(srcp, filesize);
        // free(srcp);
    }
}

void get_filetype(char *filename, char *filetype) {
    if (strstr(filename, ".html"))
        strcpy(filetype, "text/html");
    else if (strstr(filename, ".gif"))
        strcpy(filetype, "image/gif");
    else if (strstr(filename, ".png"))
        strcpy(filetype, "image/png");
    else if (strstr(filename, ".jpg"))
        strcpy(filetype, "image/jpeg");
    else if (strstr(filename, ".mp4"))
        strcpy(filetype, "video/mp4");
    else 
        strcpy(filetype, "text/plain");
}


void serve_dynamic(int fd, char *filename, char *cgiargs) {
    char buf[MAXLINE], *emptylist[] = { NULL };

    sprintf(buf, "HTTP/1.0 200 OK\r\n");
    Rio_writen(fd, buf, strlen(buf));                                                       // client fd로 요청 성공 헤더 전송
    sprintf(buf, "Server : Tiny Web Server \r\n");
    Rio_writen(fd, buf, strlen(buf));                                                       // client fd로 요청 성공 헤더 전송

    if (Fork() == 0) {
        setenv("QUERY_STRING", cgiargs, 1);                                                 // QUERY_STRING에 cgiargs에 받아온 값을 집어넣어준다
        Dup2(fd, STDOUT_FILENO);                                                            // client fd와 서버의 입출력을 동기화
        Execve(filename, emptylist, environ);                                               // CGI 프로그램 시작
    }
    Wait(NULL);
}

void echo(int connfd) {
    size_t n;
    char buf[MAXLINE];
    rio_t rio;

    Rio_readinitb(&rio, connfd);
    while((n = Rio_readlineb(&rio, buf, MAXLINE)) != 0) {
        printf("==============echo test=============\n");
        if(strcmp(buf, "\r\n") == 0)
            break;
        printf("==============echo test=============\n");
        Rio_writen(connfd, buf, n);
    }
}