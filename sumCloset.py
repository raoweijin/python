class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    def __cmp__(self, other):
        if self.value == other.value:
            return self.pos - other.pos
        return self.value - other.value 
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

        
    def subarraySumClosest(self, nums):
        # write your code here
        s = []
        s.append(Node(0, -1))
        sum = 0
        for x in range(len(nums)):
            sum += nums[x]
            s.append(Node(sum, x))
            print(sum, end= " ")
        print("")
        s = sorted(s,key=lambda node:node.value)
        #print("s is ",s)
        #s.sort()
        results= [0,0]
        ans = 1000000000000
        for i in range(len(s)-1):
            if s[i+1].value - s[i].value < ans or \
                s[i+1].value - s[i].value == ans and \
                min(s[i+1].pos, s[i].pos) + 1 < results[0]:
                print("results is ", results, "min pos is ",min(s[i+1].pos, s[i].pos) + 1)
                ans = s[i+1].value - s[i].value
                results[0] = min(s[i+1].pos, s[i].pos) + 1          
                results[1] = max(s[i+1].pos, s[i].pos)

        return results
        
data = [-3, 1, 1, -3, 5,-2]
print("data is ",data)
mySol= Solution()
res = mySol.subarraySumClosest(data)
print("res is ",res)