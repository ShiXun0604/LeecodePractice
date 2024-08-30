from lib.binary_tree import *


class Solution:
    def getMinimumDifference(self, root:TreeNode) -> int:
        a, b, c = 100001, 100001, 100001
        if root.left:
            a = self.getMinimumDifference(root.left)
        else:
            return root.val


        print(root.val)
        
        
        return 
        






root = TreeNode(4 ,TreeNode(2 ,TreeNode(1), TreeNode(3)), TreeNode(6))
solution = Solution()
ans = solution.getMinimumDifference(root)

print(ans)