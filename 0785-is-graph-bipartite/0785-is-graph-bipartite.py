from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        l = len(graph)
        q = deque()
        colArr = [-1]*l
        
        for j in range(l) :
            if colArr[j] == -1 :
                q.append(j)
                colArr[0] = 0
                while q :
                    node = q.popleft()
                    for i in graph[node] :
                        if colArr[i] == -1 :
                            colArr[i] = 1 - colArr[node]
                            q.append(i)
                        elif colArr[i] == colArr[node] :
                            return False
        return True
