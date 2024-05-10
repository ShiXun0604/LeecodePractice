from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if root == None:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))


solution = Solution()
ans = solution.invertTree(BST_0)