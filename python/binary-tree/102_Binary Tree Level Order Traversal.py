from lib.binary_search_tree import TreeNode
from lib.BST_example import *
import queue



class Solution:
    def levelOrder(self, root:TreeNode) -> list[list[int]]:
        if root == None:
            return []
        
        ans = []
        index = 0
        q = queue.Queue()

        q.put(root)
        index = 0
        while not q.empty():
            n = q.qsize()
            ans.append([])
            for i in range(n):
                node = q.get()
                ans[index].append(node.val)

                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)
            index += 1
        return ans
            

solution = Solution()
ans = solution.levelOrder(BST_2)
print(ans)