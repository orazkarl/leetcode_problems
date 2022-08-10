class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        first_str, last_str = strs[0], strs[-1]
        prefix = ''
        for i in range(len(min(first_str, last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break
        return prefix
