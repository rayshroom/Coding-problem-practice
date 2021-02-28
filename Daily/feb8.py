'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        while root is not None:
            if root.right is None:
                if root.left is None:
                    output.append(root.val)
                else:
                    output.append(root.val)
                    root = root.left
            else:
                output.append(root.val)
                root = root.right

        return output