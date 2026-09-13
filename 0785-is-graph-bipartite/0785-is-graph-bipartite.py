from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        #BFS
        # l = len(graph)
        # q = deque()
        # colArr = [-1]*l
        
        # #Always check for the discontinued graph
        # for j in range(l) :
        #     if colArr[j] == -1 :
        #         q.append(j)
        #         colArr[0] = 0
        #         while q :
        #             node = q.popleft()
        #             for i in graph[node] :
        #                 if colArr[i] == -1 :
        #                     colArr[i] = 1 - colArr[node]
        #                     q.append(i)
        #                 elif colArr[i] == colArr[node] :
        #                     return False
        # return True

        #DFS
        l = len(graph)
        vis = [-1]*l
        def dfs(node,col) :
            vis[node] = col
            for i in graph[node] :
                if vis[i] == -1 :
                    if dfs(i,1-col) == False : return False
                elif vis[i] == vis[node] :
                    return False
        for j in range(l) :
            if vis[j] == -1 :
                if dfs(j,0) == False : return False
        return True