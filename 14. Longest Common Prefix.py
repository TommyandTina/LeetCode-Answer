from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            #if first element (prefix) does not match strs[i]  -> cut the last char until it match
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
        return prefix