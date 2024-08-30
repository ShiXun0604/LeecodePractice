from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def hasPathSum(self, root:TreeNode, targetSum: int) -> bool:
        # edge case
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


solution = Solution()
ans = solution.hasPathSum(BST_2, 75)
print(ans)