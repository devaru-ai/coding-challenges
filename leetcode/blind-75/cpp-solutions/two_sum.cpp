#include <unordered_map>
#include <vector>
using namespace std;

class Solution{
public:
  vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int, int> lookup; // number-index map
    for (int i = 0; i<nums.size(); ++i){
      int needed = target - nums[i];
      if(lookup.count(needed)){
        return{lookup[needed], i};
      }
      lookup[nums[i]] = i;
    }
    return {};
  }
};
