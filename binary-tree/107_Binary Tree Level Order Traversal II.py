from lib.binary_search_tree import TreeNode
from lib.BST_example import *
import queue



class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        ans = []
        if root == None:
            return []

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            row = []
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                row.append(node.val)
            ans.append(row)
        return ans[::-1]


ans = Solution().levelOrderBottom(BST_2)
print(ans)