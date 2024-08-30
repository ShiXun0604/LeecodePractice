from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def minDepth(self, root:TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1        
        else:
            l, r = 9999, 9999
            if root.left:
                l = self.minDepth(root.left)                
            if root.right:
                r = self.minDepth(root.right)
            return min(l, r) + 1


solution = Solution()
ans = solution.minDepth(BST_2)
print(ans)