
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        buff=[[],[]]
        num = len(triangle)
        if num == 1:
            return triangle[0][0]
        res = []
        buff[0] = [triangle[0][0]]
        ping = 1
        size = 2
        for j in range(1, num):
            pang = (ping +1) %2
            numofLine = len(triangle[j])            
            buffPing = [0 for _ in range(numofLine)]
            buff[ping] = buffPing
            
            for i in range(numofLine): 
                print(" j , i are ",j,i)
                
                if i ==0:
                    buff[ping][i] = buff[pang][i]+ triangle[j][i]
                elif i == numofLine-1:
                    buff[ping][i] = buff[pang][i-1] + triangle[j][i]
                elif (i >0 ) and (i < (numofLine -1)):
                   
                    buff[ping][i] = min(buff[pang][i-1], buff[pang][i])+ triangle[j][i]
            print("buff is ",buff)
            ping = pang
        return min(buff[(ping+1)%2])

data =[[1],[9,3],[4,5,6]]
print("data is ",data)
mySol = Solution()
res = mySol.minimumTotal(data)
print("res is ", res)