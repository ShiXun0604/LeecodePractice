from lib.binary_search_tree import TreeNode
from lib.BST_example import *

class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        # edge case
        if not root:
            return
        
        first = root
        while first:
            node = first
            next_first = None
            prev = None
            while node:
                if node.left:
                    if not next_first:
                        next_first = node.left
                        prev = node.left
                    else:
                        prev.next = node.left
                        prev = node.left
                if node.right:
                    if not next_first:
                        next_first = node.right
                        prev = node.right
                    else:
                        prev.next = node.right
                        prev = node.right
                node = node.next
            first = next_first
            


root = TreeNode(1,left=TreeNode(1))
solution = Solution()
solution.connect(root)

print(root.next)
print(root.left.next)
