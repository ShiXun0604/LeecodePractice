class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # edge case
        if not nums:
            return 0
        # Sliding window
        left_ptr = 0
        right_ptr = 0
        min_len = len(nums) + 1
        sum = 0

        while right_ptr < len(nums):
                        
            if sum < target:
                sum += nums[right_ptr]
                right_ptr +=1
            else:
                sum -= nums[left_ptr]
                left_ptr +=1
                min_len = min(min_len, right_ptr-left_ptr+1)
        
        while sum >= target:
            sum -= nums[left_ptr]
            left_ptr +=1
        min_len = min(min_len, right_ptr-left_ptr+1)

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len



target = 7 
nums = [2,3,1,2,4,3]
solution = Solution()
ans = solution.minSubArrayLen(target, nums)
print(ans)