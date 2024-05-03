class Solution:
    def isPalindrome(self, s: str) -> bool:
        right_ptr = len(s) - 1
        left_ptr = 0

        while right_ptr>left_ptr:
            while not s[left_ptr].isalnum() and right_ptr>left_ptr:
                left_ptr += 1
            while not s[right_ptr].isalnum() and right_ptr>left_ptr:
                right_ptr -= 1

            if s[right_ptr].lower() != s[left_ptr].lower():
                return False

            left_ptr += 1
            right_ptr -= 1
        
        return True

s = "A man, a plan, a canal: Panama"

solution = Solution()
ans = solution.isPalindrome(s)
print(ans)


