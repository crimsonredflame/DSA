# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None :
            return []
        dq = deque()
        dq.append(root)
        res = []
        while dq :
            l = len(dq)
            arr = []
            for i in range(l) :
                ele = dq.popleft()
                if ele.left :
                    dq.append(ele.left)
                if ele.right :
                    dq.append(ele.right)
                arr.append(ele.val)
            res.append(arr)
        return res