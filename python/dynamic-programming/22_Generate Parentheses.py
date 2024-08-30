class Solution:
    def __init__(self) -> None:
        self.ans = []
    def __helper(self, left, right, result) -> None:
        if left == 0:
            self.ans.append(result + (")"*right))
            return
        
        self.__helper(left-1, right, result+"(")
        if left < right:
            self.__helper(left, right-1, result+")")

    def generateParenthesis(self, n: int) -> list[str]:
        self.__helper(n,n, "")
        return self.ans





ans = Solution().generateParenthesis(2)
print(ans)
