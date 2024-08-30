class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Two pointers
        i = 0
        j = len(numbers)-1

        print(i, j)
        summary = numbers[i] + numbers[j]
        while summary != target:
            if summary > target:
                j -= 1
            else:
                i += 1
            summary = numbers[i] + numbers[j]
        return [i+1, j+1]
        

numbers = [2,3,4]
target = 6
ans = Solution().twoSum(numbers, target)
print(ans)