class Solution {
public:
    // 1. Trie node definition
    struct TrieNode {
        TrieNode* children[26] = {};
        string word = "";
    };
    
    // 2. Insert a word into the Trie
    void insert(TrieNode* root, const string& word) {
        TrieNode* node = root;
        for(char ch: word) {
            int idx = ch - 'a';
            if (!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->word = word;
    }
    
    // 3. DFS to search for words on the board
    void dfs(vector<vector<char>>& board, int row, int col, TrieNode* node, vector<string>& result) {
        char ch = board[row][col];
        if (ch == '#' || !node->children[ch - 'a']) return;
        node = node->children[ch - 'a'];
        
        // If word found, add to result and mark as found to avoid duplicate answers
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word = "";
        }
        
        board[row][col] = '#'; // Mark as visited

        // Directions: right, left, down, up
        int dirs[4][2] = { {0,1}, {0,-1}, {1,0}, {-1,0} };
        for (auto& d : dirs) {
            int newRow = row + d[0], newCol = col + d[1];
            if (newRow >= 0 && newRow < board.size() &&
                newCol >= 0 && newCol < board[0].size()) {
                dfs(board, newRow, newCol, node, result);
            }
        }

        board[row][col] = ch; // Restore cell
    }
    
    // 4. Main function that puts everything together
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> result;
        int m = board.size(), n = board[0].size();
        TrieNode* root = new TrieNode();

        // Build the Trie with the given word list
        for (const string& word : words)
            insert(root, word);

        // Start DFS search from every cell
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) 
                dfs(board, i, j, root, result);

        return result;
    }
};
