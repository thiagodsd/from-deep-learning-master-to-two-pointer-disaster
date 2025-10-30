"""
Given an integer array nums, return an output array res where, for each value nums[i], res[i] is the first number to the right that's larger than nums[i]. If no larger number exists
to the right of nums[i], set res[i] to -1.

Example:
Input: nums = [5, 2, 4, 6, 1]
Output: [6, 4, 6, -1, -1]
"""

# thsoudu cannot solve
# the solution involves to convert the problem into to find the next largest element, starting from the right side of the array
def solution(nums:list) -> list:
    res = [0] * len(nums)
    stack = list()
    for index in range(len(nums)-1, -1, -1):
        while (stack) and (stack[-1] <= nums[index]):
            stack.pop()
        res[index] = stack[-1] if stack else -1
        stack.append(nums[index])
    return res
