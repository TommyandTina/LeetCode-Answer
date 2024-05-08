class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s if char.isalnum()).lower()
        return clean_text == clean_text[::-1]