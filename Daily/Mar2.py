'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
'''


# utilize sum of squares from 1 to n
# let x be dupe and y be missing
# sum(nums) - sum(1..n) = y - x
# sum(num^2) - sum(1..n^2) = y^2 - x^2
# get y+x from above answers, then both y and x
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        total = l*(l+1)//2 - sum(nums)
        sqrtotal = l*(l+1)*(2 * l + 1)//6 - sum(i*i for i in nums)
        y = (sqrtotal//total - total) // 2
        x = (sqrtotal//total + total) // 2
        return [y, x]