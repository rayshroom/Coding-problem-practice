/*
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1


*/

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int i = 0, j = 0, top = 0;
        int pushlen = pushed.size();
        while (i < pushlen) {
            if (top >= 0 && popped[j] == pushed[top]) {
                j++;
                top--;
            } else {
                top++;
                i++;
                if (i < pushlen) pushed[top] = pushed[i];
            }
        }
        return top == 0;
    }
};