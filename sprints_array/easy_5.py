'''
Find the Maximum Element in an Array
Write a function to return the largest value in an integer array.

Reverse an Array In-Place
Implement a function to reverse all the elements of a given array without using extra space.

Remove Duplicates from an Array
Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.

Find the Second Largest Element
Write code to identify the second largest number within an array.

Merge Two Sorted Arrays
Given two sorted arrays, merge them to form a single sorted array (do not use built-in sort).
'''
def maxElem(a: List[int]) -> int:
    max = 0
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max

def maxElem(a: List[int]) -> int:
    return max(a)

def reverseArray(a: List[int]):
    left, right = 0, len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


def duplicates(a: List[int]) -> List[int]:
    i = 1
    while i < len(a):
        if a[i] == a[i-1]:
            a.pop(i)
        else:
            i += 1
    return a

def second_largest(arr):
    max1 = max2 = float('-inf')
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x < max1:
            max2 = x
        return max2 if max2 != float('-inf') else None


def mergeSortedArray(A, B):
    i, j = 0, 0
    a = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            a.append(A[i])
            i += 1
        else:
            a.append(B[j])
            j += 1
    
    a.extend(A[i:])
    a.extend(B[j:])
    return a





