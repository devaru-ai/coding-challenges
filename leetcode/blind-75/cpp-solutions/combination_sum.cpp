class Solution {
public: 
  void backtrack(vector<int>& candidates, int target, vector<vector<int>>& res, vector<int>& comb, int start) {
    if (target==0) {
      res.push_back(comb);
      return;
    }
    if(target<0) return;
    for (int i = start, i < candidates.size(); i++) {
      comb.push_back(candidates[i]);
      backtrack(candidates, target - candidates[i], res, comb, i);
      comb.pop_back();
    }
  }
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> res;
    vector<int> comb;
    backtrack(candidates, target, res, comb, 0);
    return res;
  }
};
