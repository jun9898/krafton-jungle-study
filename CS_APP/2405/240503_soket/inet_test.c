#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>

int main(void) {
    char ip_addr_str[] = "107.212.96.29";
    struct in_addr ip_addr_bin;

    if (inet_pton(AF_INET, ip_addr_str, &ip_addr_bin) == 1) {
        printf("Conversion success\n");
        printf("Binary IP address: 0x%08" PRIX32 "\n", ntohl(ip_addr_bin.s_addr));
    } else {
        printf("Conversion failed\n");
    }

    return 0;
}