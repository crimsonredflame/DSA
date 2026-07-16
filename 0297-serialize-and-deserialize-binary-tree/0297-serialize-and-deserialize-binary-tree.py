# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None :
            return ""
        res = [str(root.val)]
        dq = deque()
        dq.append(root)
        while dq :
            ele = dq.popleft()
            if ele.left : 
                dq.append(ele.left)
                res.append(str(ele.left.val))
            else :
                res.append('N')
            if ele.right :
                dq.append(ele.right)
                res.append(str(ele.right.val))
            else :
                res.append('N')
        return ','.join(res)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data :
            return []
        arr = data.split(',')
        q = deque()
        root = TreeNode()
        root.val = int(arr[0])
        q.append(root)
        i = 1
        while q and i<len(arr) :
            ele = q.popleft()
            if i<len(arr) and arr[i] != 'N' :
                ele.left = TreeNode(int(arr[i]))
                q.append(ele.left)
            i+=1
            if i<len(arr) and arr[i] != 'N' :
                ele.right = TreeNode(int(arr[i]))
                q.append(ele.right)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))