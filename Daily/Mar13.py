'''
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.
'''

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        factors = {}
        rlt = 0
        for i in arr:
            options = 1
            upperLim = sqrt(i)
            for f1 in arr:
                if f1 > upperLim:
                    break
                f2 = i / f1
                if f2 in factors:
                    options += factors[f1] * factors[f2] * (1 if f1 == f2 else 2)
            factors[i] = options
            rlt += options
        return rlt % (10**9 + 7)