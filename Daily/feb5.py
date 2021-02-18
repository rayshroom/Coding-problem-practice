'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
'''

from collections import Counter

class Solution:
    # def findLHS(self, nums: List[int]) -> int:
    def findLHS(self, nums) -> int:
        visited = Counter(nums)

        max_val = 0
        for i in visited:
            if (i + 1) in visited:
                max_val = max(max_val, visited[i] + visited[i+1])

        return max_val

soln = Solution()

print(soln.findLHS([1,3,2,2,5,2,3,7]))