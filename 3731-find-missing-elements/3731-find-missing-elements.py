class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        mi , ma = nums[0],nums[0]
        dum_map = {}
        for i in nums:
            mi = min(mi,i)
            ma = max(ma,i)
            dum_map[i] = 0
        res = []
        for i in range(mi,ma+1) :
            if i not in dum_map :
                res.append(i)
        return res