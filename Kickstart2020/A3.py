'''
Given a list of N strictly increasing +ve integers

Define score of the list to be the maximum difference between any two
consecutive integers

Insert upto K integers to minimize the score of the list
'''

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))