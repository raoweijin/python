class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
    
    def dfs(self, s, stringlist):
        if len(s) == 0: self.res.append(stringlist)
        for i in range(1, len(s)+1):
            #if self.isPalindrome(s[:i]):
            if True:
                self.dfs(s[i:], stringlist+[s[:i]])
            
    def partition(self, s):
        self.res = []
        self.dfs(s, [])
        return self.res
data="123"
print(data)
mySolution=Solution()
res = mySolution.partition(data)
print(res)