from lib.binary_search_tree import TreeNode



class Solution:
    def __init__(self) -> None:
        self.hash_table = {}

    def __gen_tree(self, start:int, end:int) -> list[TreeNode]:
        if start > end:
            return [None]
        elif start == end:
            self.hash_table[(start, end)] = [TreeNode(start)]
            return [TreeNode(start)]
        elif (start, end) in self.hash_table.keys():
            return self.hash_table[(start, end)]
        else:
            ans = []
            for i in range(start, end+1):
                l = self.__gen_tree(start, i-1)
                r = self.__gen_tree(i+1, end)
                for a in l:
                    for b in r:
                        ans.append(TreeNode(i, a, b))

            self.hash_table[start, end] = ans
            return ans

    def generateTrees(self, n: int) -> list[TreeNode]:
        return self.__gen_tree(1, n)


ans = Solution().generateTrees(3)
print(ans)