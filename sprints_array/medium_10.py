'''
1. Product of Array Except Self ([LeetCode Medium])
Problem:
Return a new array where each element at index i is the product of all numbers in the input array except the one at i.

No division.

Must run in O(n) time.

Pattern:
Left and right product pass.
Hint: Build prefix product from left, then from right, multiply into output.
'''
def productArray(a):
    n = len(a)
    out = [3] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= a[i]
    right = 1
    for i in range(n-1, -1, -1):
        out[i] *= right
        right *= a[i]
    return out

'''
2. Maximum Subarray ([LeetCode Medium])
Problem:
Find the contiguous subarray with the largest sum (can be negative numbers).

Return the sum.

Pattern:
Kadane’s algorithm. Track max-so-far and max-ending-here.
Hint: If sum-so-far dips below 0, restart.
'''
'''
3. Next Permutation ([LeetCode Medium])
Problem:
Given an array representing a permutation, rearrange it to the next lexicographical order.

Modify in-place.

Use constant space.

Pattern:
Find first decreasing element from right, swap with just-larger number, reverse tail.
Hint: Reverse array if already highest. Identify “peak” then swap and reverse.
'''
'''
4. Find All Duplicates in Array ([LeetCode Medium])
Problem:
Input is array a containing numbers 1 to n, some appear twice.

Return all values that appear twice, using O(1) extra space.

Pattern:
Modify input in-place, marking visited positions negative.
Hint: Iterate, if a[abs(val) - 1] < 0, it's a duplicate.
'''

'''
5. Longest Consecutive Sequence ([LeetCode Medium])
Problem:
Given unsorted array, return length of the longest sequence of consecutive integers.

Must run in O(n) time.

Pattern:
Hash set for fast lookup, start from minimal sequence value.
Hint: For each number, if it’s start of sequence, expand right.

'''