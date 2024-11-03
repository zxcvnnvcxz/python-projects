# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        print(f"Inverting Node: {root.val}")
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def print_tree(node):
    if not node:
        return "none"
    return f"({node.val}, {print_tree(node.left)}, {print_tree(node.right)})"

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    solution = Solution()
    inverted_root = solution.invertTree(root)
    print(print_tree(inverted_root))