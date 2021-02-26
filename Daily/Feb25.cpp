/*
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

*/

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        std::ios::sync_with_stdio(false); std::cin.tie(nullptr);
        int len = nums.size();
        int lb = len - 1, rb = 0, _max = nums[0], _min = nums[len - 1];

        for(int i = 1; i < len; i++) {
            if (_max > nums[i]) {
                rb = i;
            } else {
                _max = nums[i];
            }

            if (_min < nums[len - i]) {
                lb = len - i;
            } else {

                _min = nums[len - i];
            }
        }

        if (_min < nums[0]) lb = 0;

        return rb == lb ? 0 : max(0, rb - lb + 1);
    }
};