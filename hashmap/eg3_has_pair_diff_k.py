# Given an array of integers and an integer k, determine if there are any two numbers in the array whose difference is k. Return True if such a pair exists, otherwise False.

def hasPairWithDifferenceK(nums, K):
    num_set = set(nums)
    for num in nums:
        if (num+k) in num_set or (num-k) in num_set:
            return True
    return False