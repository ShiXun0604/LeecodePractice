from lib.binary_tree import *

class Solution:
    # recursive
    def maxDepth(self, root:TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

solution = Solution()
ans = solution.maxDepth(root)
print(ans)