import time

class Solution:
    def jump(self, nums: list[int]) -> int:        
        curr = 0
        step = 0
        start, end = curr+1, curr+nums[curr]
        while curr<len(nums)-1:
            #print('開始與結束位置：', start, end)
            start, end = curr+1, curr+nums[curr]
            
            if end >= len(nums):
                step +=1
                break
            # find next step
            Max = 0
            while start<=end and start<len(nums):
                if nums[start] > Max:
                    Max = nums[start]
                    curr = start
                start +=1
                
            step += 1
        return step
            


nums = [0]
ans = Solution().jump(nums)
print(ans)