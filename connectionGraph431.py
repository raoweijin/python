
#Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []



class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        nodeSet=[]
        for ie in nodes:
            flag = False;
            flag = self.find(ie,nodeSet)
            if flag == False:
                newSet = set()
                self.bfs(ie,newSet)
                nodeSet.append(newSet)
        print("nodeset", nodeSet)
        return nodeSet
                
    def find(self, node, setList):
            for ie in setList:
                if node.label in ie:
                    return True                   
                    
            return False
            
    def bfs(self, node, nodeSet)        :
            q=[]
            q.append(node)
            while q!= []:
                actNode= q.pop(0)
                nodeSet.add(node.label)
                for ie in node.neighbors:
                    q.append(ie)
                    
                    
                    
                
mysol = Solution()
a= UndirectedGraphNode(2)
nodeList=[a]
mysol.connectedSet(nodeList)
            
        
