class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        self.__generateTrees(1, n)



ans = Solution().generateTrees(1)
print(len(ans))