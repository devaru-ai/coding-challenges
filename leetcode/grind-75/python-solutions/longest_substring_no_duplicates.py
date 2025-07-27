class Solution:
  def lengthOfLongestSubstring(self, s:str) -> int:
    last_index = {}
    max_len = 0
    start = 0
    for end, c in enumerate(s):
      if c in last_index and last_index[c] >= start:
        start = last_index[c]+1
      last_index[c] = end
      max_len = max(max_len, end - start + 1)
    return max_len
