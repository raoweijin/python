class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 1
        if n <= 2:
            return n
        result=[1,2]

        for i in range(n-2):
            print("result is ",result)
            print("result[-2] and [-1]",result[-2],result[-1] )
            result.append(result[-2]+result[-1])
        return result
        
mySol = Solution()
n = 4
res = mySol.climbStairs(n)
print("result is ",res)