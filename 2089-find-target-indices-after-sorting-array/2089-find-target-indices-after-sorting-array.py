class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m , n = 0 , 0
        for i in range(len(nums)) :
            if nums[i] == target :
                m += 1
            if nums[i] < target :
                n += 1
        res = []
        for i in range(m) :
            res.append(n+i)
        return res