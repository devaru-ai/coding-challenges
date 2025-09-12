class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != str[0][i]:
                    return s[:1]
            i += 1
        return s[:1]