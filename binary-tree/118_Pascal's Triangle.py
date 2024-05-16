class Solution:
    def __init__(self) -> None:
        self.hash_table = {
            1 : [[1]],
            2 : [[1], [1, 1]],
        }
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows in self.hash_table.keys():
            return self.hash_table[numRows]
        
        arr = [1]
        prev_arr = self.generate(numRows-1)
        for i in range(len(prev_arr[-1])-1):
            arr.append(prev_arr[-1][i]+prev_arr[-1][i+1])
        arr.append(1)
        prev_arr.append(arr)
        return prev_arr



ans = Solution().generate(5)
print(ans)