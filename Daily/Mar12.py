'''
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.
'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSubstring = set()
        for i in range(len(s) - k + 1):
            uniqueSubstring.add(s[i:i+k])
            
        return len(uniqueSubstring) == 2 ** k