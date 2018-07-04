import sys
import collections

# a wall 2, an house 1 or empty 0
 
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxsize for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxsize 
        #min_dist = 9999999999999999
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
        print("reachable_count is ", reachable_count)
        print("dist is ",dist)
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxsize  else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)])
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxsize :
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1 
data=[[0,1,2],[0,0,1],[1,2,2]]
print("data is ")
for ie in data:
    print(ie)
#print(data)
node =[1,1]
deltaNode=((1,0),(-1,0),(0,1),(0,-1))
for dx,dy in deltaNode:
    nwNode=(node[0] + dx,node[1] + dy)
    print("new Node ",nwNode)
mySolution = Solution()
res = mySolution.shortestDistance(data)
print(res)