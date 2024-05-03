class Solution:
    def removeDuplicates(self, nums:list[int]) -> int:
        # edge case
        if not nums:
            return 0

        # Two pointer
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j+1







nums = [0,0,1,1,1,2,2,3,3,4,6,6,10,50]
solution = Solution()
ans = solution.removeDuplicates(nums)
print(ans)
print(nums)
