'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lb, rb, max_ = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                lb += 1
            else:
                rb += 1
                
            if lb == rb:
                max_ = max(max_, 2 * lb)
            elif rb >= lb:
                lb = 0
                rb = 0
                
        lb = 0
        rb = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                lb += 1
            else:
                rb += 1
                
            if lb == rb:
                max_ = max(max_, 2 * lb)
            elif lb >= rb:
                lb = 0
                rb = 0
                
        return max_
