from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def helper(L:TreeNode, R:TreeNode) -> bool:
            if L == None and R == None:
                return True
            elif L == None or R == None:
                return False
            return (L.val == R.val) and helper(L.left, R.right) and helper(L.right, R.left)

        return helper(root.left, root.right)


