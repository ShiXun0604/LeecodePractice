class Solution(object):
    def rob(self, nums):
        rob = 0
        not_rob = 0

        for num in nums:
            cur_rob = not_rob + num
            not_rob = max(not_rob, rob)
            rob = cur_rob
        
        return max(rob, not_rob)