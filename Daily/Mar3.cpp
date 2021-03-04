/*

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), m = nums.size();
        for(int i = 0; i < m; i++) {
            n ^= (nums[i] ^ i);
        }
        return n;
    }
};