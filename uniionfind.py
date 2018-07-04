
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree1(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        from Queue import Queue
        queue = Queue()
        
        queue.put(0)
        visited[0] = True
        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.put(node)

        return len(visited) == n

        
        
    def validTree(self, n, edges):
        # Write your code here
        root = [i for i in range(n)]
        for i in edges:
            root1 = self.find(root, i[0])
            root2 = self.find(root, i[1])
            print("node0,node1",i[0],i[1])
            print("root1,root2", root1, root2)
            if root1 == root2:
                return False
            else:
                root[root1] = root2
            print("root", root)  
            print("*********************")
        print("root",root)
        return len(edges) == n - 1
        
    def find(self, root, e):
        if root[e] == e:
            return e
        else:
            root[e] = self.find(root, root[e])
            return root[e]
            
edges=[[0,1],[1,2],[0,2]]
#edges=[[2,0],[2,3],[2,4],[0,1]]
edges=[[0,1],[1,2],[8,0]]
n= 4

mysolution = Solution()
res = mysolution.validTree(n,edges)
print(res)