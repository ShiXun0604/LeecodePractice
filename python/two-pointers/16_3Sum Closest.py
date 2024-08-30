class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        mini = float('inf')

        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l_ptr = i + 1
            r_ptr = len(nums) - 1
            while l_ptr < r_ptr:
                num = nums[i] + nums[l_ptr] + nums[r_ptr]
                if abs(num-target) <= mini:
                    ans = num
                    mini = abs(num-target)
                
                if num > target:
                    r_ptr -= 1
                else:
                    l_ptr += 1
        return ans






nums = [-1,2,1,-4]
ans = Solution().threeSumClosest(nums, 1)
print(ans)