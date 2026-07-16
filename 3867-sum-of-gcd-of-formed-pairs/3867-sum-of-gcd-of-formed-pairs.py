class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a,b) :
            return a if b==0 else gcd(b,a%b)
        arr = []
        maxi = float('-inf')
        for i in nums :
            maxi = max(i,maxi)
            arr.append(gcd(maxi,i))
        arr.sort()
        
        sum = 0
        l = len(arr) - 1
        for i in range(len(arr)//2) :
            sum+= gcd(arr[i],arr[l-i])
        return sum
