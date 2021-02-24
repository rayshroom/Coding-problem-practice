class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int h = matrix.size(), w = matrix[0].size();
        int r = h - 1, c = 0;
        while (c < w && r >= 0) {
            if (matrix[r][c] == target) return true;

            matrix[r][c] < target ? c++ : r--;
        }
        
        return false;
    }
};

int main() {
    Solution soln = new Solution();
}