/*

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

*/

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int dp[amount + 1];
        
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            dp[i] = INT_MAX;
        }
        
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= i) {
                    int sub = dp[i - coins[j]];
                    if (sub != INT_MAX && sub + 1 < dp[i]) {
                        dp[i] = sub + 1;
                    }
                }
            }
        }
        
        if (dp[amount] == INT_MAX) return -1;
        return dp[amount];
    }
};
