from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def __init__(self) -> None:
        self.last = None
        self.minimum = 1000000

    def inorder_traversal(self, root):
        if root.left:
            self.inorder_traversal(root.left)

        if self.last != None:
            self.minimum = min(self.minimum, root.val-self.last)
        self.last = root.val

        if root.right:
            self.inorder_traversal(root.right)

    def getMinimumDifference(self, root:TreeNode) -> int:
        self.inorder_traversal(root)
        return self.minimum


solution = Solution()
ans = solution.getMinimumDifference(BST_0)
print(ans)
