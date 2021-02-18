'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
'''

import itertools

class Solution:
    def letterCasePermutation(self, S):
        return list(set(map(''.join, itertools.product(*zip(S.upper(), S.lower())))))


soln = Solution()
print(soln.letterCasePermutation("a1b2"))