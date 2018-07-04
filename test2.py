import copy
Class Solution:
    def combinationSum(self, candidates, target):
        self.line=[]
        self.res=[]
        return res;
    def helper(self, data, target):
        if 0== target:
            return
        
        for ie in data:
            temp = target - ie
            if temp > 0:
                self.line.append(ie)
                child = self.helper(data,temp)
                self.line.pop(ie)
            elif temp == 0:

                self.line.append(buff)
                buff=copy.deepcopy(self.line)
                self.res.append(self.line)
                self.line.pop()
                self.
                return
            else:
                return;