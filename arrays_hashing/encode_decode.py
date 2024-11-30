"""
Encode and Decode Strings
Solved
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for st in strs:
            encoded_str += str(len(st)) + '#' + st

        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            lt = ""
            while s[i] != '#':
                lt += s[i]
                i += 1
            i += 1
            j = i + int(lt)
            strs.append(s[i:j])
            i = j

        return strs