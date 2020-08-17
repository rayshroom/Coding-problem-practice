'''
Find length of Longest Increasing Sequence (LIS) of a list

E.g.
LIS of 1,6,2,3,7,5
is 1,2,3,5
length is 4

Note that LIS is not consecutive
'''

# let the input be a comma seperated line of integers
numbers = list(map(int, input().split(',')))
size = len(numbers)
# let f[i] represent the length of LIS when ending with i_th element
f = [1] * size

for i in range(size):
    for j in range(i):
        # transition: for each ai > aj, f[i] = f[j] + 1
        if (numbers[j] < numbers[i]):
            f[i] = max(f[i], f[j] + 1)

ans = 0
for i in f:
    ans = max(ans, i)

print(f'Length of LIS: {ans}')