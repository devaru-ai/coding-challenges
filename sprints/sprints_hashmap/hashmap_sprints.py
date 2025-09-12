'''
1. Given an array of integers nums and an integer k, write a function to return the integer that appears most frequently in any sliding window of size k. If multiple values tie for highest frequency, return the smallest such integer.

Example:

Input: nums = [2, 3, 2, 4, 3, 2, 5], k = 3

Windows: [2,3,2], [3,2,4], [2,4,3], [4,3,2], [3,2,5]

In the first window, 2 appears twice—highest; in the last window, also 2; in the others, all numbers appear once.

Output: 2
'''

from typing import List
from collections import defaultdict

def mostFreqElementK(nums: List[int], k: int) -> int:
    freq_map = defaultdict(int)

    # Initialize frequency map for the first window
    for i in range(k):
        freq_map[nums[i]] += 1

    # Determine the most frequent element in initial window
    max_count = 0
    result = None
    for num, count in freq_map.items():
        if count > max_count or (count == max_count and (result is None or num < result)):
            max_count = count
            result = num
    
    # Slide window
    for i in range(k, len(nums)):
        freq_map[nums[i]] += 1
        freq_map[nums[i-k]] -= 1
        # Scan current window for most frequent element
        cur_window_max = 0
        cur_window_num = None
        for num, count in freq_map.items():
            if count > cur_window_max or (count == cur_window_max and (cur_window_num is None or num < cur_window_num)):
                cur_window_max = count
                cur_window_num = num

        if cur_window_max > max_count or (cur_window_max == max_count and cur_window_num < result):
            max_count = cur_window_max
            result = cur_window_num

    return result

'''
2. Longest Subarray with Sum ≤ Target
Given nums and an integer target, return the length of the longest contiguous subarray whose sum is less than or equal to target.

Input: nums = [1, 2, 3, 2, 1], target = 5

Output: 3
'''
def longestSubarray(nums: List[int], target: int) -> int:
    start = 0
    window_sum = 0
    max_len = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum > target and start<=end:
            window_sum -= nums[start]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

'''
3. Maximum Average Subarray of Size k
Given nums and integer k, return the maximum average possible for any contiguous subarray of size k.

Input: nums = [5, 1, 3, 8, 10, 2], k = 3

Output: 7
(Subarray [3,8,10] has sum 21, average 7)
'''
def maxAvgSubarray(nums: List[int], k: int) -> int:
    window_sum = 0
    max_sum = 0

    for i in range k:                   # window_sum = sum(nums[:k]) 
        window_sum += nums[i]

    max_sum = max(window_sum, max_sum)  # max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(window_sum, max_sum)

    return max_sum // k

'''
4. Minimum Window Size with All Unique Values
Find the minimum size window (contiguous subarray) containing every unique value present in nums.

Example Input: nums = [1, 2, 3, 2, 1, 4]

Distinct values: {1, 2, 3, 4} (so window must contain all four)
'''
from typing import List
from collections import defaultdict

def minWindowAllDistinct(nums: List[int]) -> int:
    required_set = set(nums)
    required_count = len(required_set)
    counter = defaultdict(counter)

    min_len = float('inf')
    start = 0
    end = 0

    while end < len(nums):
        counter[nums[end]] += 1
        end += 1
        
        while all(counter[val]>0 for val in required_set):
            min_len = min(min_len, end - start)
            counter[nums[start]] -= 1
            start += 1
    return min_len if min_len != float('inf') else 0