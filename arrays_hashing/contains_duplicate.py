"""
Contains Duplicate
Solved
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for num in nums:
            if unique.get(num) is None:
                unique[num] = 1
            else:
                unique[num] += 1

        for value in unique.values():
            if value > 1:
                return True
        return False

