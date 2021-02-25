#include <stack>

class Solution {
public:
    int scoreOfParentheses(string S) {
        stack<int> s;
        s.push(0);
        int ans = 0;
        for (char const &c : S) {

            if (c == '(') {
                s.push(0);
            } else {
                int curr = s.top();
                s.pop();
                int prev = s.top();
                s.pop();
                ans = prev + (curr * 2 > 1 ? curr * 2 : 1);
                s.push(ans);
            }
        }
        return ans;
    }
};