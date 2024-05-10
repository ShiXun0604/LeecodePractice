from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:     
    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        # edge case
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        
solution = Solution()
ans = solution.isSameTree(BST_2, BST_0)
print(ans)