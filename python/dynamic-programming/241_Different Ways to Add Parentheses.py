class Solution:
    def __init__(self) -> None:
        self.hash_table = {}

    def diffWaysToCompute(self, expression: str) -> list[int]:
        ans = []
        if expression in self.hash_table.keys():
            return self.hash_table[expression]

        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                ans_l = self.diffWaysToCompute(expression[:i])
                ans_r = self.diffWaysToCompute(expression[i+1:])
            
                for l in ans_l:
                    for r in ans_r:
                        if expression[i] == '+':
                            ans.append(l + r)
                        elif expression[i] == '-':
                            ans.append(l - r)
                        elif expression[i] == '*':
                            ans.append(l * r)

        if not ans:
            ans.append(int(expression))
        self.hash_table[expression] = ans
        return ans

expression = "2*3-4*5"
print(Solution().diffWaysToCompute(expression))