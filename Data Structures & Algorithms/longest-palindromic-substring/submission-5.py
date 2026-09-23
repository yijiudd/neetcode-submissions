class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        max_len=1    
        
        dp= [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)-2,-1,-1):
            for j in range(1,len(s)):
                if i>j:
                    continue
                if i==j:
                    dp[i][j]=True
                    
                elif s[i]==s[j] and (dp[i+1][j-1] or j-i<=2):
                    dp[i][j]=True
                    if j-i+1>max_len:
                        start=i
                        max_len=j-i+1
        return s[start:start+max_len]


        