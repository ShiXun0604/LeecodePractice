class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        r_mapping = {}

        data = s.split(' ')

        if len(data) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mapping.keys():
                mapping[pattern[i]] = data[i]
                r_mapping[data[i]] = pattern[i]

            elif mapping[pattern[i]] != data[i]:
                return False
        
        if len(mapping.keys()) != len(r_mapping.keys()):
            return False
        return True
            


pattern = "aaa"
s = "aa aa aa aa"

solution = Solution()
ans = solution.wordPattern(pattern, s)
print(ans)