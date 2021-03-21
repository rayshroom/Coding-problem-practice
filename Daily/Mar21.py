'''
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.
'''

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # 2^29 < 10^9 < 2^30
        base = 1
        n = len(str(N))
        while len(str(base)) < n:
            base *= 2
        
        while len(str(base)) == n:
            if sorted(str(base)) == sorted(str(N)):
                return True
            base *= 2
            
        return False
