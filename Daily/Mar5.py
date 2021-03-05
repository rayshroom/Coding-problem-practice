'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        lvlQ = [root]
        rlt = []
        while len(lvlQ) != 0:
            tmpQ = []
            sum_ = 0
            for i in lvlQ:
                sum_ += i.val
                if i.left is not None:
                    tmpQ.append(i.left)
                if i.right is not None:
                    tmpQ.append(i.right)
                    
            rlt.append(sum_ / len(lvlQ))
            lvlQ = tmpQ
            
        return rlt
        