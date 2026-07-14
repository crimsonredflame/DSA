# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        dq = deque()
        dq.append((0,0,root))
        m = defaultdict(lambda : defaultdict(list))
        while dq :
            ver,lev,node = dq.popleft()
            if node.left : dq.append((ver-1,lev+1,node.left))
            if node.right : dq.append((ver+1,lev+1,node.right))
            m[ver][lev].append(node.val)
        res = []
        for i in sorted(m.keys()) :
            col = []
            for j in sorted(m[i].keys()) :
                col.extend(sorted(m[i][j]))
            res.append(col)
        return res