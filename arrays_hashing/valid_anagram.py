"""
Valid Anagram
Solved
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = defaultdict(lambda: 0)

        for c in s:
            char_map[c] += 1

        for c in t:
            if char_map.get(c) == None:
                return False
            char_map[c] -= 1

        for v in char_map.values():
            if v != 0:
                return False

        return True