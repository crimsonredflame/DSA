class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        so = 1
        se = 2
        for i in range(n-1) :
            so = so + 2*(i+1) + 1
            se = se + 2*(i+2)
        def gcd(a,b) :
            return a if b == 0 else gcd(b,a%b)
        g = gcd(so,se)
        return g