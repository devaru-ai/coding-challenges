# Given a list of lowercase letters, return the number of distinct characters that occur an odd number of times.

def countOddOccurences(chars):
    freq_map = {}
    for char in chars:
        freq_map[char] = freq_map.get(char, 0) + 1
    odd_count = 0
    for count in freq_map.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count


# return an array of characters that occur an odd number of times instead of count.

def charWithOddOccurences(chars):
    freq_map = {}
    for char in chars:
        freq_map[char] = freq_map.get(char, 0) + 1
    odd_chars = []
    for char, count in freq_map.items():
        if count % 2 != 0:
            odd_chars.append(char)
    return odd_chars