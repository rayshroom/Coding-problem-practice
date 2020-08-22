'''
Give a list of integers, find the number of peaks
'''

T = int(input())
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    peaks = 0
    for i in range(1, N - 1):
        if (heights[i] > heights[i-1]) and (heights[i] > heights[i+1]):
            peaks += 1

    print('Case #{}: {}'.format(_ + 1, peaks))