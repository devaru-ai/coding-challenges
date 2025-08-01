class Solution {
public:
    // Return the minimum window substring of s that contains all characters of t (including duplicates)
    string minWindow(string s, string t) {
        unordered_map<char, int> need, window;

        // 1. Count how many of each character is needed 
        for (char c : t) need[c]++;

        int left = 0, right = 0; // Window [left, right]
        int valid = 0;           // How many characters have the correct count in the current window
        int start = 0;           // Start index of the best (smallest) window found
        int len = INT_MAX;       // Length of the best window

        // 2. Move the right side of window forward, picking up characters
        while (right < s.size()) {
            char c = s[right];
            right++; // Expand window to the right

            // If the character is needed, add it to the window
            if (need.count(c)) {
                window[c]++;
                // If you now have exactly as many as needed for this char, count it as "valid"
                if (window[c] == need[c]) valid++;
            }

            // 3. When the window has all needed characters (for every needed char, the count matches)
            while (valid == need.size()) {
                // Update smallest window if this one is smaller
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }

                // Try to shrink the window from the left side to see if we can get even smaller
                char d = s[left];
                left++;
                if (need.count(d)) {
                    // If we are about to remove a character that was just enough, window is less valid now
                    if (window[d] == need[d]) valid--;
                    window[d]--;
                }
            }
        }
        // 4. If no window was found, return "", else return the answer substring
        return len == INT_MAX ? "" : s.substr(start, len);
    }
};
