class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagramGroups;
    for(auto& word : strs) {
      string shape = word; // Copy original word
      sort(shape.begin(), shape.end()) //Sort letters
      anagramGroups[shape].push_back(word); // Add to group
    }
    vector<vector<string>> result;
    for (auto& group: anagramGroups) {
      result.push_back(group.second); // Add each grp to result
    }
    return result;
  }
};
