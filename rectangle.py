"""
class Point:
    def __init__( self, x=0, y=0):
       	self.x = x
       	self.y = y
"""
class Solution:
    """
    @param pointSet: The point set
    @return: The answer
    """
    def rectangle(self, pointSet):
        verLine={}
        OrtLine={}
        verFlag = False;
        OrtFlag = False;
        for id,ie in enumerate(pointSet):
            if verLine.has_key(ie.x):
                verLine[ie.x].add(id)
            else:
                verLine[ie.x]=set()
                verLine[ie.x].add(id)
            if OrtLine.has_key(ie.y):
                OrtLine[ie.y].add(id)
            else:
                OrtLine[ie.y]=set()
                OrtLine[ie.y].add(id)
                
        #print(OrtLine)
        numV = 0
        numO=0
        for ie in verLine:
            if len(verLine[ie])<2:
                verLine.remove(ie)
        if len(verLine) <2:
            return "NO"
        
        
        for ie in verLine:
            for id in ie:
                yval= pointSet[id].y
                if OrtLine.has_key(yval):
                    OrtLine[yval]+=1
                else:
                    OrtLine[yval] =1
        for ie in OrtLine
            if OrtLine[ie]>1:
                numO+=1
                if numO> 1:
                    print(ie)
                    OrtFlag= True
                    break
        if OrtFlag:
            return "YES"
        else:
            return "NO"