class Solution {
public:
  int hammingWeight(unint32_t n) {
    int count = 0;
    while(n) {
      count += (n&1);
      n >>= 1;
    }
    return count;
  }
};
