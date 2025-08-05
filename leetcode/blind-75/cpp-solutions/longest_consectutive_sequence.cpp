#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    if(nums.empty())
      return 0;
    unordered_set<int> num_set(nums.begin(), nums.end());
    int max_streak;

    for(int num : num_set){
      // check if the num is the start of sequence
      if(!num_set.count(num-1)) {
        int current_num = num;
        int current_streak = 1;
        // extend the sequence
        while(num_set.count(current_num+1)){
          current_num += 1;
          current_streak += 1;
        }
        max_streak = max(max_streak, current_streak);
      }
    }
    return max_streak;
  }
};
