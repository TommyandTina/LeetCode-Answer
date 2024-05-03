class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack) #aaab
        n = len(needle)   #b
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

#another solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)