class Solution:
    def lengthOfLongestSubstring(self, s: str)-> int:
        l = 0
        longest = 0
        hashset = set()
        n = len(s)

        for r in range(n):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            
            w = (r-l) + 1
            longest = max(longest, w)
            hashset.add(s[r])
        
        return longest