class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #first make adjacency list
        # graph = [[] for i in range(numCourses)]
        # for a,b in prerequisites :
        #     graph[b].append(a)

        # vis = [False]*numCourses
        # pathvis = [False]*numCourses

        # #dfs
        # def dfs(node) :
        #     vis[node] = True
        #     pathvis[node] = True
        #     for i in graph[node] :
        #         #when node has not been visited
        #         if not vis[i] :
        #             if dfs(i) : return True
        #         #when node has been visited but has been visited on the same path
        #         elif pathvis[i] : return True
        #     pathvis[node] = False
        #     return False
        
        # res = False
        # for i in range(numCourses) :
        #     if not vis[i] :
        #         if dfs(i) : 
        #             res = True
        # return not res

        
        # for bfs code we see if topo sort geverated is a valid topo sort if not then cycle exits

        cnt = 0
        graph = [[] for i in range(numCourses)]
        
        for a,b in prerequisites :
            graph[a].append(b) 
        indeg = [0]*numCourses
        for i in graph :
            for j in i :
                indeg[j] += 1
        q = deque()
        for i in range(numCourses) :
            if indeg[i] == 0:
                q.append(i)
        while q :
            node = q.popleft()
            cnt+=1
            for i in graph[node]:
                indeg[i]-=1
                if indeg[i] == 0: q.append(i)
        if cnt == numCourses :
            return True
        return False
        