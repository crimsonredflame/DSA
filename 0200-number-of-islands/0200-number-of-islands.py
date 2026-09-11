from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        vis = [[0]*n for i in range(m)]
        def bfs(row,col) :
            vis[row][col] = 1
            q = deque()
            q.append([row,col])
            while q :
                row , col = q.popleft()
                dir = [(-1,0),(0,-1),(1,0),(0,1)]
                for i,j in dir :
                    nrow = row + i
                    ncol = col + j
                    if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                        vis[nrow][ncol] = 1
                        q.append([nrow,ncol])

        cnt = 0 
        for i in range(m) :
            for j in range(n) :
                if not vis[i][j] and grid[i][j] == '1' :
                    cnt += 1
                    bfs(i,j)

        return cnt