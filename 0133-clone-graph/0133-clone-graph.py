"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None : return None

        m = {}
        def dfs(n) :
            if n in m :
                return m[n]
            copy = Node(n.val)
            m[n] = copy
            for i in n.neighbors :
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node)

        