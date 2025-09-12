def freqConsecutiveSubarray(self, nums: List[int])->int:
    hash_map = {}
    for i in range(len(nums)-1):
        pair = (nums[i], nums[i+1])
        hash_map[pair] = hash_map.get(pair, 0) + 1
    return max(hash_map.values()) if hash_map else 0