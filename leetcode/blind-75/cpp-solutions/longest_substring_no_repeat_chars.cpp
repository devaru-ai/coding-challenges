#include <unordered_map>
#include <string>
using namespace std;

class Solution{
public:
  int lengthOfLongestSubstring(string s){
    unordered_map<char, int> lastIndex;
    int maxLen = 0;
    int start = 0;
    // Walk through each character
    for (int end = 0; end < s.length(); ++end){
      char c = s[end];
      // If we've seen this char inside current window
      if(lastIndex.count(c) && lastIndex[c] >= start){
        start = lastIndex[c] + 1;
      }
      lastIndex[c] = end; // Update or add the char's latest index
      maxLen = max(maxLen, end - start + 1);
    }
    return maxLen;
  }
};
