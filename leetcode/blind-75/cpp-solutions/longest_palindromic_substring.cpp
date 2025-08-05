#include <string>
using namespace std;

class Solution{
public:
  string longestPalindrome(string s) {
    int n = s.size();
    if(n == 0)
      return "";
    int start = 0, maxLen = 1;
    auto expand = [&](int left, int right){
      while(left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
      }
      int len = right - left + 1;
      if(len > maxLen) {
        maxLen = len;
        start = left + 1;
      }
    };
    for (int center = 0; center < n; ++center) {
      expand(center, center);
      expand(center, center+1);
    }
    return s.substr(start, maxLen);
  }
};

      
