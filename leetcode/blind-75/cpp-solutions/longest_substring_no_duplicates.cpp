#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

//Given a string, find the length of the longest substring with no duplicate characters.
class Solution {
public:
  int lengthOfLongestSubstring(string s){
    unordered_map<char, int> lastIndex; // Maps each char to its most recent index
    int maxLen = 0;
    int start = 0;

    // Expand the sliding window[start, end]
    for(int end = 0; end < s.length(); ++end) {
        char c = s[end];

        // If 'c' was seen before and is within the current window, move start right after its prev occurrence.
        if (lastIndex.count(c) && lastIndex[c] >= start) {
            start = lastIndex[c] + 1;
        }
      
        // Update the last seen index of 'c'.
        lastIndex[c] = end;
      
        // Update the max len if current window is longer.
        maxLen = max(maxLen, end - start + 1);
    }
    return maxLen;
  }
