'''
Given a list of integers, find the maximum sum of any sublist

e.g.
-2,1,-3,4,-1,2,1,-5,4

sum[4,-1,2,1] = 6    <-- maximum sum
'''


numbers = list(map(int, input().split(',')))
size = len(numbers)
# let f[i] represent the current maximum sum of list ending at position i
f = [0] * size

ans = 0
for i in range(1, size):
    # if previous sum is less than 0, then we can ignore the previous sum as
    # it will not be benefitial to next sublist
    f[i] = max(f[i - 1], 0) + numbers[i]
    ans = max(ans, f[i])

print(ans)

