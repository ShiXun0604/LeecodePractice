from lib.binary_search_tree import TreeNode
from lib.BST_example import *



class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if preorder == []:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        BST = TreeNode(preorder[0])
        # divide and conquer
        index = inorder.index(preorder[0])
        inorder_L = inorder[0:index]
        inorder_R = inorder[index+1:len(inorder)]
        preorder_L = preorder[1:1+len(inorder_L)]
        preorder_R = preorder[1+len(inorder_L):len(preorder)]
        
        BST.left = self.buildTree(preorder_L, inorder_L)
        BST.right = self.buildTree(preorder_R, inorder_R)
        return BST


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
ans = solution.buildTree(preorder, inorder)

