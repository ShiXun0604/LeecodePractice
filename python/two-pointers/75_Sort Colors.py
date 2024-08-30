class Solution:
    def sortColors(self, nums: list[int]) -> None:
        i = 0
        j = len(nums) - 1
        p = 0
        while p <= j:
            print(nums, i, j ,p)
            if nums[p] == 2:
                nums[p] = nums[j]
                nums[j] = 2
                j -= 1
                p -= 1
            elif nums[p] == 0:
                nums[p] = nums[i]
                nums[i] = 0
                i +=1
            p += 1
            






nums = [1,2,0]
Solution().sortColors(nums)
print(nums)
