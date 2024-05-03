#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    struct addrinfo hints, *res, *p;
    int status;
    char ipstr[INET6_ADDRSTRLEN];

    if (argc != 3) { // 입력 인자가 3개(프로그램 이름, 호스트 이름, 서비스 이름)가 아니면 사용법 출력 후 종료
        fprintf(stderr, "Usage: %s host service\n", argv[0]);
        return 1;
    }

    memset(&hints, 0, sizeof hints); // hints 구조체 초기화
    hints.ai_family = AF_UNSPEC; // IPv4 또는 IPv6 주소 모두 허용
    hints.ai_socktype = SOCK_STREAM; // TCP 스트림 소켓

    if ((status = getaddrinfo(argv[1], argv[2], &hints, &res)) != 0) { // getaddrinfo 함수 호출
        fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(status)); // 실패 시 에러 메시지 출력
        return 2;
    }

    printf("IP addresses for %s:%s\n\n", argv[1], argv[2]); // 입력받은 호스트와 서비스 이름 출력

    for (p = res; p != NULL; p = p->ai_next) { // 반환된 주소 정보 연결 리스트 순회
        void *addr;
        char *ipver;

        // IPv4 또는 IPv6 주소 얻기
        if (p->ai_family == AF_INET) { // IPv4 주소인 경우
            struct sockaddr_in *ipv4 = (struct sockaddr_in *)p->ai_addr;
            addr = &(ipv4->sin_addr);
            ipver = "IPv4";
        } else { // IPv6 주소인 경우
            struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *)p->ai_addr;
            addr = &(ipv6->sin6_addr);
            ipver = "IPv6";
        }

        // IP 주소를 문자열로 변환
        inet_ntop(p->ai_family, addr, ipstr, sizeof ipstr); // 바이너리 IP 주소를 문자열로 변환
        printf(" %s: %s\n", ipver, ipstr); // IP 버전과 문자열 주소 출력
    }

    freeaddrinfo(res); // 반환된 연결 리스트 메모리 해제

    return 0;
}