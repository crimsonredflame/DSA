class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                if s[i-1] == t[j-1] :
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return m == dp[m][n]