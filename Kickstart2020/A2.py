'''
Problem
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ K ≤ 30.
1 ≤ P ≤ N * K.
The beauty values are between 1 and 100, inclusive.

Test set 1
1 ≤ N ≤ 3.

Test set 2
1 ≤ N ≤ 50.

Sample

Input
 	
Output
 
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10
'''

testCases = int(input())
for _ in range(testCases):
    stacks, stackSize, quota = map(int, input().split())

    plates = []
    for j in range(stacks):
        plates.append(list(map(int, input().split())))

    # precompute stack sum, let sum[i][x] denote sum of first x plates in the i_th stack
    s = [[0] * stackSize for x in range(stacks)]
    for j in range(stacks):
        s[j][0] = plates[j][0]
        for x in range(1, stackSize):
            s[j][x] = s[j][x - 1] + plates[j][x]

 

    dp = [[0] * quota for x in range(stacks)]
    for i in range(stacks):
        for j in range(quota):
            for x in range(min(j, stackSize)):
                dp[i][j] = max(dp[i][j], s[i][x] + dp[i-1][j-x])

    print('Cast #{}: {}'.format(_, dp[-1][-1]))
