from typing import Optional




class Solution:
    # Optimal Solution
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if root is None:
            return 0

        leftHeight = self.dfsHeight(root.left)

        rightHeight = self.dfsHeight(root.right)

        if leftHeight == -1:
            return -1

        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1


if __name__ == "__main__":
    Tree = TreeNode([1,2,2,3,3,None,None,4,4])