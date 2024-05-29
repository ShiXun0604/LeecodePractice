class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans_dict = {}
        ans = []
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l_ptr = i + 1
            r_ptr = len(nums) - 1
            while l_ptr < r_ptr:
                num = nums[i] + nums[l_ptr] + nums[r_ptr]
                if num == 0:
                    name = '{}, {}, {}'.format(nums[i], nums[l_ptr], nums[r_ptr])
                    if name not in ans_dict.keys():
                        ans_dict[name] = ''
                        ans.append([nums[i], nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1
                    r_ptr -= 1
                elif num > 0:
                    r_ptr -= 1
                elif num < 0:
                    l_ptr += 1
        return ans
                

        




nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print(ans)