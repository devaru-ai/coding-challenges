class Solution{
public:
  int countSubstring(string s) {
    int n = s.size();
    int count = 0;
    auto countAroundCenter = [&] (int left, int right) {
      while(left > = 0 && right < n && s[left] == s[right]) {
        count++;
        left--;
        right++;
      }
    };
    for(int center = 0; center < n; ++center) {
      countAroundCenter(center, center);
      countAroundCenter(center, center+1);
    }
    return count;
  }
};
