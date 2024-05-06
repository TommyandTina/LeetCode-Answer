#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* addBinary(char* a, char* b) {
    int i = strlen(a) - 1;
    int j = strlen(b) - 1;
    int carry = 0;
    char* result = (char*)malloc(10240 * sizeof(char));
    int k = 10239;
    result[k--] = '\0';
    while(i >= 0 || j >= 0 || carry > 0) {
        int sum = carry;
        if(i >= 0) sum += a[i--] - '0';
        if(j >= 0) sum += b[j--] - '0';
        carry = sum / 2;
        result[k--] = (sum % 2) + '0';
    }
    return result + k + 1;
}

int main() {
    char a[] = "11";
    char b[] = "1";
    char* result = addBinary(a, b);
    printf("Output: %s\n", result);
    free(result);
    return 0;
}

/*
+ '0' là chuyển số thành chữ số, - '0' là chuyển chữ số thành số
*/