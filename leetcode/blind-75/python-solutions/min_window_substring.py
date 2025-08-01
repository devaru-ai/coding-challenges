class Solution(object):
    def minWindow(self, s, t):
        # Example: s = "ABCBCD", t = "AC"
        
        from collections import Counter
        
        # Count how many of each character we need from t
        # e.g., t = "AC" -> need = {'A':1, 'C':1}
        need = Counter(t)
        
        # Total number of characters from t that we need to find
        missing = len(t)
        
        left = 0            # Left pointer for window start
        start = end = 0     # Start/end indices of the best (smallest) window found so far
        
        # Move right pointer through each character in s
        for right, char in enumerate(s): 
            # If this char is still needed, then we reduce the number we are missing
            if need[char] > 0:
                missing -= 1
            
            # Subtract from need dict, even if we have an extra of this char
            need[char] -= 1

            # When we have found all required chars (including duplicates)
            if missing == 0:
                # Try to shrink window from the left, skip chars that are not needed or in excess
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # Update best window if the current one is smaller
                if end == 0 or right - left < end - start:
                    start, end = left, right+1  # right+1 because end is exclusive in slice

                # Prepare for next possible window: this removes the leftmost char (which is required)
                need[s[left]] += 1
                missing += 1
                left += 1

        # Return the smallest window found, or "" if no window found
        return s[start:end]
