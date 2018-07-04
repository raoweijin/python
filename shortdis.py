import sys
import collections

# a wall 2, an house 1 or empty 0
 
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        m = len(grid)
        n = len(grid[0])    
        self.dis= [[0 for i in range(m)] for j in range(n)]
        self.reachCount = [[0 for i in range(m)] for j in range(n)]

        res=[]
        #dis=[]
        reachCount=[]

        house = []
        houseNum = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    houseNum+=1
                    house.append((i,j))
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 0):
                    node = (i,j)
                    #area = (m,n)
                    self.bfs(node,grid)
        
        print("houseNum is ",houseNum)
        print("house is ",house)
        print("distance is ",self.dis)
        print("reachCount is ",self.reachCount)
        return res
    def bfs(self,node,grid):
        m = len(grid)
        n = len(grid[0])
        detaLoc = ((1,0),(-1,0),(0,1),(0,-1));
        q=[]
        q.append([node,0])
        visited = [[False for i in range(m)] for j in range(n)]
        print("visited", visited)
        #print("q1 is ",q)
        #print("node is ", node,"888888888888888888888888888888888888888888888888888888888888888")
        while q != []:
            print("q is ", q,"88888888888")
            qMember = q.pop(0)
            actNode = qMember[0]
            tempDis = qMember[1]
            for ie in detaLoc:
                newNode = [actNode[0]+ie[0],actNode[1]+ie[1]]
                x = newNode[0]
                y = newNode[1]
                #print("new Node",x,y, visited[x][y])
                if x >=0 and y >=0 and x < m and y < n:                    
                    
                    if visited[x][y] == False:
                        visited[x][y]= True
                        #print("new node visit will be true",x,y)
                        #print("visisted is ",visited)
                        if grid[x][y] ==0:
                            q.append([newNode,tempDis+1])
                        elif  grid[x][y] ==1:
                            x1  = node[0]
                            y1  = node[1]
                            
                            self.dis[x1][y1] = self.dis[x1][y1]  + (tempDis+1)
                            #print("self.dis is ",self.dis ,self.dis[x1][y1])
                            self.reachCount[x1][y1] +=1

                
        return
        
data=[[0,1,2],[0,2,1],[1,2,2]]
print("data is ")
for ie in data:
    print(ie)
#print(data)
mySolution = Solution()
mySolution.shortestDistance(data)

