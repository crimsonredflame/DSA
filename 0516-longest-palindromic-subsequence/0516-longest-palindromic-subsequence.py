class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        rev = s[::-1]
        if s == rev :
            return m
        dp = [[0]*(m+1) for i in range(m+1)]

        for i in range(1,m+1) :
            for j in range(1,m+1) :
                if s[i-1] == rev[j-1] :
                    dp[i][j] = 1+dp[i-1][j-1]
                else :
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
        return dp[m][m]