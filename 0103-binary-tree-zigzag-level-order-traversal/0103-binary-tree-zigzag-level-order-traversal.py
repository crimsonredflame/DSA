# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None :
            return []
        dq = deque()
        dq.append(root)
        flag = 0
        res = []
        arr = []
        while dq :
            l = len(dq)
            for i in range(l) :
                el = dq.popleft()
                if el.left : dq.append(el.left)
                if el.right : dq.append(el.right)
                arr.append(el.val)
            if flag == 0 :
                res.append(arr)
                flag = 1
            else :
                res.append(arr[::-1])
                flag = 0
            arr = []
        return res
