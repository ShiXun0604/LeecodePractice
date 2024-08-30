class Solution:
    def __init__(self) -> None:
        self.hash_table = {}

    def __is_palindrome(self, s:str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return [[]]
        elif s in self.hash_table.keys():
            return self.hash_table[s]
        
        result = []
        for i in range(1,len(s) + 1):
            if self.__is_palindrome(s[:i]):
                for r in self.partition(s[i:]):
                    result.append([s[:i]] + r)

        self.hash_table[s] = result
        return result






