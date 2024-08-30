class Solution:
    # Boyer–Moore majority vote algorithm
    def majorityElement(self, nums: list[int]) -> int:
        num = nums[0]
        cnt = 1

        for i in range(1,len(nums)):
            if num == nums[i]:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                num = nums[i]
                cnt = 1
        
        return num
    
    # Hash map algorthm
    def majorityElement2(self, nums: list[int]) -> int:
        num_dict = {}

        for n in nums:
            if n not in num_dict.keys():
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        
        r_num_dict = {}
        for i in num_dict.keys():
            r_num_dict[num_dict[i]] = i
        
        return r_num_dict[max(r_num_dict.keys())]




nums = [3,2,3,3,3,3,3,3,3,5,7,4,1,8]
solution = Solution()
ans = solution.majorityElement2(nums)
print(ans)