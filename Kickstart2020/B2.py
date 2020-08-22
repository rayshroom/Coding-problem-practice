'''
Bucket is planning to make a very long journey across the countryside by bus. Her journey consists of N bus routes, numbered from 1 to N in the order she must take them. The buses themselves are very fast, but do not run often. The i-th bus route only runs every Xi days.

More specifically, she can only take the i-th bus on day Xi, 2Xi, 3Xi and so on. Since the buses are very fast, she can take multiple buses on the same day.

Bucket must finish her journey by day D, but she would like to start the journey as late as possible. What is the latest day she could take the first bus, and still finish her journey by day D?
'''

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    lstX = list(map(int, input().split()))

    startDay = D
    for i in reversed(lstX):
        startDay = min(startDay, startDay // i * i)
    
    print('Case #{}: {}'.format(_ + 1, startDay))
    