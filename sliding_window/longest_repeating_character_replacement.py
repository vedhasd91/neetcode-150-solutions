"""
Longest Repeating Character Replacement
Solved
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        freq = defaultdict(int)

        # Crux windowLen - Count[MostFreqChar] <= k
        while r < len(s):
            freq[s[r]] += 1
            maxf = freq[max(freq, key=freq.get)]

            while (r - l + 1 - maxf) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

            # print(l,r, res)

        return res