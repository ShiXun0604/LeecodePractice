class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def __init__(self) -> None:
        # (start, end) -> [Tree_1, ..., Tree_n]
        self.hash_table = {

        }

    def __generateTrees(self, start, end) -> list[TreeNode]:
        if (start, end) in self.hash_table.keys():
            return self.hash_table[(start, end)]
        elif start > end:
            return [None]
        else:
            ans = []
            for i in range(start, end+1):
                
                # start ~ i-1
                L_subtrees = self.__generateTrees(start, i-1)
                # i+1 ~ end
                R_subtrees = self.__generateTrees(i+1, end)

                # Combine tree
                for l in L_subtrees:
                    for r in R_subtrees:
                        ans.append(TreeNode(i, l, r))

            self.hash_table[(start, end)] = ans
            return ans
        
    def generateTrees(self, n: int) -> list[TreeNode]:
        for i in range(1, n+1):
            self.hash_table[(i ,i)] = [TreeNode(i)]

        ans = self.__generateTrees(1, n)
        return ans



ans = Solution().generateTrees(5)
print(ans)