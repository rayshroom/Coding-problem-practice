'''
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
'''

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A, reversed=True)
        B = sorted([(b, i) for i, b in enumerate(B)], reversed=True)
        rlt = [-1] * len(A)
        
        start = 0
        end = len(A) - 1
        
        for b, i in B:
            if A[start] > b:
                rlt[i] = A[start]
                start += 1
            
            else:
                rlt[i] = A[end]
                end -= 1
                
        return rlt
