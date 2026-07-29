# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def form(st,en,nums) :
            if st > en : 
                return None
            mid = (st+en)//2
            root = TreeNode(nums[mid])
            root.left = form(st,mid-1,nums)
            root.right = form(mid+1,en,nums)
            return root
        return form(0,len(nums)-1,nums)

            