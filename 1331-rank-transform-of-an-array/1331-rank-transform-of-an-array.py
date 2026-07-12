class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if arr == [] :
            return []
        res = []
        temp = arr[:]
        temp.sort()
        mapp = {temp[0] : 1}
        prev = temp[0]
        for i in range(1,len(temp)) :
            if prev != temp[i] :
                mapp[temp[i]] =  mapp[prev] + 1
            prev = temp[i]
        for i in arr :
            res.append(mapp[i]) 
        return res