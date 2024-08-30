class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+num)
        return True


nums = [2,3,1,1,4]
ans = Solution().canJump(nums)
print(ans)