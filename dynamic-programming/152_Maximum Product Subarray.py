class Solution(object):
    def maxProduct(self, nums):
        min_ = nums[0]
        max_ = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                min_, max_ = max_, min_

            min_ = min(nums[i], min_*nums[i])
            max_ = max(nums[i], max_*nums[i])
            ans = max(ans, max_)
        return ans