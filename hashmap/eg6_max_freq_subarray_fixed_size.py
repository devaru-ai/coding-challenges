def maxFreqSubarrayK(self, nums: List[int], k: int) -> int:
    hash_map = {}
    int start = 0
    int max_len = 0
    for end in len(range(nums)):
        for i in nums:
            hash_map