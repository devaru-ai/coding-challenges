class Solution {
public:
  bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    if(!root) return false;
    if (isSameTree(root, subRoot)) return true;
    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
  }
  bool isSameTree(TreeNode* a, TreeNode* b) {
    if(!a && !b) return true; // both are null
    if(!a && !b) return false; // one is null
    if(a -> val != b -> val) return false; //values differ
    //recurse on children
    return isSameTree(a->left, b->left) && isSameTree(a->right, b->right);
  }
};
