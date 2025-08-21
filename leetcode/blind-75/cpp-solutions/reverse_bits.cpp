class Solution {
public:
  unint32_t reverseBits(unint32_t n) {
    unint32_t result = 0;
    for(int i = 0; i<32; ++i) {
      result <<= 1;              // Shift result left to make space
      result |= (n&1);           // Copy in rightmost bit of n
      n >>= 1;                    // Shift n right
    }
    return result;
  }
};
