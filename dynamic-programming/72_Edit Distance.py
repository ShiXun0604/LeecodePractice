class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        msg = [i for i in range(len(word1)+1)]
        
        for i in range(1, len(word2)+1):
            print(msg)
            prev = msg[0]
            msg[0] = i
            for j in range(1, len(word1)+1):
                a = msg[j-1] + 1
                b = msg[j] + 1
                c = prev
                if word1[j-1] != word2[i-1]:
                    c += 1
                # find best
                prev = msg[j]
                msg[j] = min(a, b, c)
        return msg[len(word1)]





word1 = "sitting"
word2 = "kitten"
ans = Solution().minDistance(word1, word2)
print(ans)