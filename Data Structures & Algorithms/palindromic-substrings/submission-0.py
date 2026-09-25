class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False]*len(s) for _ in range(len(s))]
        num=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if j-i<=1 or dp[i+1][j-1]:
                        dp[i][j]=True
                        num+=1
        return num

        