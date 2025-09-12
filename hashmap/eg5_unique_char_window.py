# Given a string, find the length of the longest substring (window) containing only unique characters.
def uniqueCharWindow(str):
    hash_map = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        char = s[end]
        if char in hash_map and hash_map[char] >= start:
            start = hash_map[char]+1
        hash_map[char] = end
        curr_window_len = end - start + 1
        max_len = max(max_len, curr_window_len)
    return max_len