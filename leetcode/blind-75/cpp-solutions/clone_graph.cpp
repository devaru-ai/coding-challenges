class Solution {
public: 
  Node* cloneGraph(Node* node){
    if(!node) return nullptr;
    unordered_map<Node*, Node*> copied;
    function<Node* (Node*)> dfs = [&](Node* curr) -> Node* {
      // If we've cloned this house already, just use the clone.
      if(copied.count(curr)) return copied[curr];
      
      // Make a new node.
      Node* clone = new Node(curr->val);
      copied[curr] = clone;
      
      // Clone all neighbors.
      for(Node* neighbor : cur->neighbors){
        clone->neighbors.push_back(dfs(neighbor));
      }
      return clone;
    };
    return dfs(node);
  }
};






















/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        
    }
};
