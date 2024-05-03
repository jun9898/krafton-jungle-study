#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>

int main(void) {
    uint32_t ip_addr_bin = 0x0A010140; // 127.0.0.1
    char ip_addr_str[INET_ADDRSTRLEN];

    if (inet_ntop(AF_INET, &ip_addr_bin, ip_addr_str, sizeof(ip_addr_str)) != NULL) {
        printf("Conversion success\n");
        printf("String IP address: %s\n", ip_addr_str);
    } else {
        printf("Conversion failed\n");
    }
    return 0;
}