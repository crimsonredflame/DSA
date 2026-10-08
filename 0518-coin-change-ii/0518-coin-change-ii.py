class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        l = len(coins)
        dp = [[0]*(amount + 1) for i in range(l+1)]
        for i in range(1,l+1) :
            dp[i][0] = 1
        for i in range(1,l+1) :
            for j in range(1,amount+1) :
                if coins[i-1] <= j :
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
        return dp[l][amount]