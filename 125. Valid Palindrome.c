#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

bool isPalindrome(char * s){
    int start = 0, end = strlen(s) - 1;
    while(start < end) {
        if(!isalnum(s[start])) {
            start++;
        } else if(!isalnum(s[end])) {
            end--;
        } else {
            if(tolower(s[start]) != tolower(s[end])) {
                return false;
            }
            start++;
            end--;
        }
    }
    return true;
}

int main() {
    char s[] = "A man, a plan, a canal: Panama";
    if(isPalindrome(s)) {
        printf("The string is a palindrome.\n");
    } else {
        printf("The string is not a palindrome.\n");
    }
    return 0;
}
