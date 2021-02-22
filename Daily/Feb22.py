'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
'''

class Solution:


    def findLongestWord(self, s: str, d: List[str]) -> str:
        rlt = ''
        for i in d:
            if len(i) < len(rlt) or (len(i) == len(rlt) and i > rlt):
                continue
            pos = -1
            for j in w:
                pos = s.find(j, pos + 1)
                if pos == -1:
                    break
            if pos != -1
                rlt = i
        return rlt