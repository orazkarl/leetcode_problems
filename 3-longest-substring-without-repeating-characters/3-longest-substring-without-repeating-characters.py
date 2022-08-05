class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght: int = 0
        for i in range(len(s)):
            temp = s[i:]
            array = []
            for char in temp:
                if char in array:
                    break
                array.append(char)
            max_lenght = len(array) if len(array) > max_lenght else max_lenght
        return max_lenght