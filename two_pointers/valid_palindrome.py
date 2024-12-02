"""
Valid Palindrome
Solved
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")

        j = len(s) - 1
        i = 0

        while i < j:
            while j > i and not s[j].isalnum():
                j -= 1
            while i < j and not s[i].isalnum():
                i += 1

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
