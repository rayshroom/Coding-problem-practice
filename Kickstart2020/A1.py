'''
Problem
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.

Limits
Time limit: 15 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ Ai ≤ 1000, for all i.

Test set 1
1 ≤ N ≤ 100.

Test set 2
1 ≤ N ≤ 105.

Sample
3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999
'''

testCases = int(input())
for i in range(testCases):
    bought = 0
    cases, budget = map(int, input().split())
    price = sorted(list(map(int, input().split())))
    for j in price:
        if j <= budget:
            budget -= j
            bought += 1
        else:
            break
    print('Case #{}: {}'.format(i + 1, bought))