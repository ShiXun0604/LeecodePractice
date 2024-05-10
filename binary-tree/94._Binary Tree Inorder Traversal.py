from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def __init__(self) -> None:
        self.array = []
    
    def __inorderTraversal(self, root:TreeNode) -> None:       
        if root.left:
            self.__inorderTraversal(root.left)
        self.array.append(root.val)
        if root.right:
            self.__inorderTraversal(root.right)

    def inorderTraversal(self, root:TreeNode) -> list[int]:
        # edge case
        if root == None:
            return []

        self.__inorderTraversal(root)
        return self.array



solution = Solution()
ans = solution.inorderTraversal(BST_2)
print(ans)
