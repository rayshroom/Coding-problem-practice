'''

Input:
N       # number of cases
w1,w2   # comma seperated pair of words
'''

cases = int(input())
for i in range(cases):
    f = [[1]]
    word1, word2 = input().split(',')