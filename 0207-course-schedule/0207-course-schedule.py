class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #first make adjacency list
        graph = [[] for i in range(numCourses)]
        for a,b in prerequisites :
            graph[b].append(a)
        vis = [False]*numCourses
        pathvis = [False]*numCourses

        #dfs
        def dfs(node) :
            vis[node] = True
            pathvis[node] = True
            for i in graph[node] :
                #when node has not been visited
                if not vis[i] :
                    if dfs(i) : return True
                #when node has been visited but has been visited on the same path
                elif pathvis[i] : return True
            pathvis[node] = False
            return False
        
        res = False
        for i in range(numCourses) :
            if not vis[i] :
                if dfs(i) : 
                    res = True
        return not res
        