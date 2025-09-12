# Given a list of integers, write a function that returns a dictionary mapping each integer to its frequency. 

def freqCounter(nums):
    hash_map = {}
    for num in nums:
        freq_map[num] freq_map.get(num, 0) + 1
    return freq_map

# Given a list of integers, write code to return the first integer that appears exactly once. If none, return -1.
def firstUnique(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    for num in nums:
        if freq_map[num] == 1:
            return num
    return -1

# Given a list of integers, count how many elements are greater than every element to their left.
def countGreaterThanLeft(nums):
    count = 0
    cur_max = float('-inf')
    for num in nums:
        if num > cur_max:
            count += 1
            curr_max = num
    return count