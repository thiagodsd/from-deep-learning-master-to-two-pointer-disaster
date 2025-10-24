"""
Given an array of integers, return the indexes of any two numbers that add up to a target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example:
- Input nums = [-1, 3, 4, 2], target = 3
- Output: [0, 2]

Explanation: nums[0] + nums[2] = -1 + 4 = 3

Constraints:
* The same index cannot be used twice in the result.
"""

# thsoudu solution
# - nao esta ordenado
def solution(nums:list, target:int) -> list:
    for i in range(len(nums)): # O(n)
        for j in range(i+1, len(nums)): # O(n-1) ~ O(n)
            result_sum = nums[i] + nums[j]
            if result_sum == target:
                return [i, j]
    return []

# O(n^2) time complexity
# O(1) space complexity

# print(solution([-1, 3, 4, 2], 3))
# print(solution([1, 4, 3], 8))
# python 01-pair-sum-unsorted.py 
# [0, 2]
# []

# thsoudu after study
def solution(nums:list, target:int) -> list:
    first_look = dict()
    for index, value in enumerate(nums): # O(n)
        first_look[value] = index
    for index, value in enumerate(nums): # O(n)
        complement = target - value
        if (complement in first_look) and (first_look[complement] != index):
            return [first_look[complement], index]
    return list()

# O(2n) time complexity
# O(n) space complexity

# print(solution([-1, 3, 4, 2], 3))
# print(solution([1, 4, 3], 8))
# [2, 0]
# []

# thsoudu optimized
def solution(nums:list, target:int) -> list:
    """
    constraint: index repetitions are not allowed
    """
    already_seen = dict() # memory -> O(n)
    for index, value in enumerate(nums): # processing -> O(n)
        complement = target - value
        if (complement in already_seen) and (index != already_seen[complement]):
            return [index, already_seen[complement]]
        already_seen[value] = index
    return list()

print(solution([-1, 3, 4, 2], 3))
print(solution([1, 4, 3], 8))
print(solution([], 8))
print(solution([-10, 5, 33, 2], -8))
print(solution([0, 1, 5, 8, 0, -1], 0))