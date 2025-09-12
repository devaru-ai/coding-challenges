# 1. Given nums = [2, 4, 2, 5, 2], write code to build a dictionary counting occurrences using only a one-liner with .get().

def dictKeyIncrement(self, nums: List[int]) -> dict[int, int]:
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    return hash_map

# 2. Given a = [5, 8, 12, 5, 6], b = [2, 5, 8], write code to return a set of elements in a that are also in b.
def setMembership(self, nums1: List[int], nums2: List[int]) -> set:
    return set(nums1) & set(nums2)
    
# 3. Given letters = ['a', 'b', 'a', 'c', 'b'], create a dictionary comprehension mapping each unique letter to its count.
def dictComprehension(self, letters: List[str]) -> dict[str, int]:
    return {char : letters.count(char) for char in set(letters)}

# set(letters) ensures each letter is counted once and appears as a key.       
# letters.count(char) gives the total count for that letter in the input list.

# 4. Given nums = [5, 3, 5, 7, 9, 3], create a dictionary mapping each unique number to its square, but only include numbers that are odd.
def filterDictMap(nums):
    return {num: num*num for num in set(nums) if num % 2 != 0}

# 5. Given d = {'a': 1, 'b': 2, 'c': 1}, write code to invert the dictionary so that each value maps to a list of associated keys.
def invertDict(d: dict[str, int]) -> dict[int, list[str]]:
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

# 6. Given list1 = [10, 12, 15, 13, 15], list2 = [15, 12, 18, 13, 21], create a set comprehension containing all values present in both lists and divisible by 3.
def setCommonElements(nums1, nums2):
    return {num for num in nums1 if num % 3 == 0} & {num for num in nums2 if num % 3 == 0}

# 7. Given scores = {'alice': 77, 'bob': 92, 'carol': 85, 'dan': 77, 'eve': 92}, build a dictionary using comprehension, containing only names whose scores are greater than 80.
def dictValueFilter(d: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in d.items() if v > 80}
            
# 8. Given s = "BaNaNa", use a set comprehension to collect all unique characters appearing in the string exactly once (respecting case sensitivity).
def uniqueChars(str):
    return {char: for char in str if s.count(char) == 1}

# 9. Input: pairs = [('cat', 'animal'), ('rose', 'flower'), ('dog', 'animal'), ('lily', 'flower')]
#    Output: {'animal': ['cat', 'dog'], 'flower': ['rose', 'lily']}
from typing import List, Tuple, Dict
def tupleToDict(List[Tuple[str, str]]) -> Dict[str, List[str]]:
    group_dict = {}
    for item, group in pairs:
        if group not in group_dict:
            group_dict[group] = [item]
        else:
            group_dict[group].append(item)
    return group_dict

# Using setdefault()
def group_items(pairs: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    group_dict = {}
    for item, group in pairs:
        group_dict.setdefault(group, []).append(item)
    return group_dict


# 10. Given pairs = [('a', 1), ('b', 2), ('c', 1), ('d', 2), ('e', 1)], build a dictionary mapping each integer to a set of associated letters.
def mapValuesToSet(pairs: List[Tuple[str, int]]) -> Dict[str, Tuple[str]]:
    set_dict = {}
    for char, num in pairs:
        set_dict.setdefault(num, set()).add(char)
    return set_dict

# 11. Given info = {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 5, 'fig': 1}, filter the dictionary to include only fruits with value greater than 2, even-valued, and whose name contains the letter 'a'.
def filterDictCombo(info: Dict[str, int]) -> Dict[str, int]:
    return {k: v for k, v in info.items() if v > 2 and v % 2 == 0 and 'a' in k}

# 12. Given words = ['robot', 'apple', 'banana', 'bat', 'armor'], use set comprehension to collect all words starting and ending with 'a'.
def setComprehension(words: List[str]) -> Set[str]:
    return {word for word in words if word.endswith('a') and word.startswith('a')}