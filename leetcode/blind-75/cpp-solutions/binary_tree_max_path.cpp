class Solution{
public:
  int max_sum; // To hold max sum found anywhere
  int dfs(TreeNode* node) {
    if(!node) return 0; // Empty tree

    // Recursively compute max path from left and right child
    int left = std::max(0, dfs(node->left));
    int right = std::max(0, dfs(node->right));

    // Max path using this node as the highest point
    int through_here = node->val + left + right;

    //Update global max_sum if this path is better
    max_sum = std::max(max_sum, through_here);

    // For recursion: node + best ONE side
    return node->val + std::max(left, right);
  }
  int maxPathSum(TreeNode* root) {
    max_sum = INT_MIN;
    dfs(root);
    return max_sum;
  }
};
