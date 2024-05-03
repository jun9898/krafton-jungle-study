#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;
    char file_name[100];
    char ch;

    // 파일 열기 시도
    fd = open("text.txt", O_RDONLY);
    if (fd == -1) {
        printf("Error opening file.\n");
        exit(1);
    }

    printf("File opened successfully. File descriptor: %d. Press Ctrl+C to exit.\n", fd); // 파일 디스크립터 출력

    // 키보드 입력 대기
    while (1) {
        // 키보드 입력 처리
        ch = getchar();
        if (ch == EOF) // Ctrl+C 입력이나 개행 문자(Enter)가 입력되면 종료
            break;
    }

    // 파일 닫기
    close(fd);
    printf("File closed.\n");

    return 0;
}