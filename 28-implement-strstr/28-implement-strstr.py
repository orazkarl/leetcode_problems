class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:len(needle) + i] == needle:
                return i
        return index