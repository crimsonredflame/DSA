# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        m = {}
        dq = deque()
        dq.append(root)
        while dq :
            ele = dq.popleft()
            if ele.left : 
                dq.append(ele.left)
                m[ele.left] = ele
            if ele.right :
                dq.append(ele.right)
                m[ele.right] = ele
            if ele.val == start :
                search = ele
        vis = {search : 0}
        dq.append(search)
        time = 1
        while dq :
            l = len(dq)
            for i in range(l) :
                ele = dq.popleft()
                #parent
                if ele in m and m[ele] not in vis :
                    vis[m[ele]] = time
                    dq.append(m[ele])
                #left child
                if ele.left and ele.left not in vis :
                    vis[ele.left] = time
                    dq.append(ele.left)
                #right child
                if ele.right and ele.right not in vis :
                    vis[ele.right] = time
                    dq.append(ele.right)
            time+=1
        return max(vis.values())
            
            
                