class Solution():
    def __rob(self, nums):
        rob = 0
        not_rob = 0

        for num in nums:
            curr_rob = not_rob + num
            not_rob = max(rob, not_rob)
            rob = curr_rob
        return max(rob, not_rob)


    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.__rob(nums[1:]), self.__rob(nums[:len(nums)-1]))