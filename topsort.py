"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""        
        
class Solution:

    @param graph: A list of Directed graph node
    @return: A list of integer
    def dfs(self,root):
        if root == None:
            return;

        for ie in root.neighbors:
            self.nodeNum[ie]+= 1
            self.dfs(ie)
    def topSort(self, graph):        
        res = []
        self.nodeNum={} 
        for ie in graph:
            self.nodeIn[ie] = 0
        for ie in graph
            for neibor in ie.neighbors:
                self.nodeIn[neibor]+=1
        for ie in self.nodeIn:
            if self.nodeIn[ie] == 0:
                res.append(ie)
                
        return res
    
      