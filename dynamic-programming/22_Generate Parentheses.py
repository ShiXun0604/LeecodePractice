class Solution:
    def __init__(self) -> None:
        self.ans = []
    def helper(self, left, right, result) -> None:
        if left == 0:
            self.ans.append(result + (")"*right))
            return
        if right == 0:
            self.ans.append(result)
            return
        
        self.helper(left-1, right, result+"(")
        if left < right:
            self.helper(left, right-1, result+")")

    def generateParenthesis(self, n: int) -> list[str]:
        self.helper(n,n, "")
        return self.ans





ans = Solution().generateParenthesis(9)
print(ans)