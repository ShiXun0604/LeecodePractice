class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def __init__(self) -> None:
        self.ans = []
    
    def __recur_gen(self, result, left, right) -> None:
        pass
        if left == 0:
            self.ans.append(result + ")"*right)
            return
        
        self.__recur_gen(result+'(', left-1, right)
        if left < right:
            self.__recur_gen(result+')', left, right-1)
        
    
    def generateParenthesis(self, n: int) -> list[str]:
        self.__recur_gen('', n, n)
        return self.ans


s = 'abab'
print(s[0:3])
