class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        maxi = max(nums)

        def gcd(a,b) :
            return a if b== 0 else gcd(b,a%b)
        return gcd(mini,maxi)