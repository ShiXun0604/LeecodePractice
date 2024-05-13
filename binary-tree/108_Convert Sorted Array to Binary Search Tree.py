from lib.binary_search_tree import TreeNode



class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid_index = int(len(nums)/2)
            l_nums = nums[0:mid_index]
            r_nums = nums[mid_index+1:len(nums)+1]
            return TreeNode(nums[mid_index],
                            left=self.sortedArrayToBST(l_nums),
                            right=self.sortedArrayToBST(r_nums)
                            )


nums = [-10,-3]
solution = Solution()
ans = solution.sortedArrayToBST(nums)