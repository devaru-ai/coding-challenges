# Given an array of integers, return True if the number of times each value occurs is unique for all values. Otherwise, return False.

def uniqueOccurences(self, nums: List[int]) -> bool:
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    freqs = set(freq_map.values())
    return len(freqs) == len(freq_map)