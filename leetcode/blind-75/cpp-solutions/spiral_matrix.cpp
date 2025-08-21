class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    if(matrix.empty()) return {};

    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;
    vector<int> result;

    while( top <= bottom && left <= right) {

      // Go right
      for(int j = left; j <= right; ++j) 
        result.push_back(matrix[top][j]);
      ++top; // done with this row

      // Go down
      for(int i = top; i <= bottom; ++i)
        result.push_back(matrix[i][right]);
      --right; //done with this column

      // Go left (only if still rows left)
      if(top <= bottom) {
        for(int j = right; j >= left; --j)
          result.push_back(matrix[bottom][j]);
        --bottom;
      }

      // Go up (only if still columns left)
      if(left <= right) {
        for(int i = bottom; i>=top; --i) 
          result.push_back(matrix[i][left]);
        ++left;
      }
    }
  return result;
  }
};


