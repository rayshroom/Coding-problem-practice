/*
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

*/

// TODO: improve this solution to use bitwise operation
class Solution {
public:
    int divide(int dividend, int divisor) {
        int minint = -2147483648, q = 0;

        if (divisor == minint) return dividend == divisor;
        
        if (dividend == minint) {
            if (divisor == minint) return 1;
            else if (divisor == -1) return -(minint+1);
            else if (divisor == 1) return minint;
            else {
                dividend += abs(divisor);
                q++;
            }
        }
        q += floor(exp(log(abs(dividend)) - log(abs(divisor))));

        return q * (dividend < 0 == divisor < 0 ? 1 : -1);
    }
};