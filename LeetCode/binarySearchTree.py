class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        root.left = self.lowestCommonAncestor(root.left, p, q)
        root.right = self.lowestCommonAncestor(root.right, p, q)

        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        else:
            return root

    def lowestCommonAncestorSorted(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the current node is None, return None
        if root is None:
            return root

        # Store the value of the current node
        value = root.val

        # If both p and q are less than the current node's value,
        # then the LCA must be in the left subtree
        if p.val < value and q.val < value:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both p and q are greater than the current node's value,
        # then the LCA must be in the right subtree
        if p.val > value and q.val > value:
            return self.lowestCommonAncestor(root.right, p, q)

        # If one of p or q is equal to the current node, or one is on
        # the left and the other is on the right, then the current node is the LCA
        return root






