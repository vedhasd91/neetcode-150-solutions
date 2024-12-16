"""
Longest Substring Without Repeating Characters
Solved
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        l = 0
        r = 0
        slen = 0

        while r < len(s):
            if s[r] in visited:
                l = max(visited[s[r]]+1,l)
            visited[s[r]] = r
            slen = max(slen, r-l+1)
            #print(l,r,s[l],s[r])
            r+=1

        return slen