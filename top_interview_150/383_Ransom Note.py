class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_dict = {}
        for i in magazine:
            if i not in word_dict.keys():
                word_dict[i] = 1
                continue

            word_dict[i] += 1
        
        for i in ransomNote:
            if i not in word_dict.keys():
                return False
            elif word_dict[i] == 0:
                return False
            else:
                word_dict[i] -=1
        
        return True



magazine = ''
ransomNote = ''
solutuin = Solution()
ans = solutuin.canConstruct(ransomNote, magazine)
print(ans)