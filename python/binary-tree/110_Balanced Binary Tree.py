from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def max_depth(self, root:TreeNode) -> int:
        if root == None:
            return 0
        else:
            left_depht = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            return max(left_depht, right_depth) + 1
        
    def isBalanced(self, root:TreeNode) -> bool:
        if root == None:
            return True
        
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        if abs(left_depth-right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False


solution = Solution()
ans = solution.connect(BST_2)
print(ans)


