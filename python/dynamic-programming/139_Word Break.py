class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for word in wordDict:
                word_len = len(word)
                if s[i-word_len: i] == word and dp[i-word_len]:
                    dp[i] = True
        return dp[-1]