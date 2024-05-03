#include <stdio.h>
#include <string.h>

int lengthOfLastWord(char* s) {
    int len = strlen(s);
    int count = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (s[i] != ' ') {
            count++;
        } else if (count > 0) {
            return count;
        }
    }
    return count;
}

int main() {
    char s[] = "Hello World";
    printf("Length of last word: %d\n", lengthOfLastWord(s));
    return 0;
}
