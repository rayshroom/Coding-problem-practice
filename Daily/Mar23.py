'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.
'''

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = collections.Counter(arr)
        keys = sorted(count)
        
        rlt = 0
        
        for i, x in enumerate(keys):
            t = target - x
            j = i
            k = len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < t:
                    j += 1
                elif y + z > t:
                    k -= 1
                else:
                    if i < j < k:
                        rlt += count[x] * count[y] * count[z]
                    elif i == j < k:
                        rlt += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        rlt += count[x] * count[y] * (count[y] - 1) // 2
                    else:
                        rlt += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                        
                    j += 1
                    k -= 1
                    
        return rlt % (10**9 + 7)
            
