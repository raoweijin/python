'''
124. Longest Consecutive Sequence 
 Description
 Notes
 Testcase
 Judge
Discuss 
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Have you met this question in a real interview? 
Clarification
Your algorithm should run in O(n) complexity.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Tags 
Related Problems 


class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        
'''        
data = [100, 4, 200, 1, 3, 2]        
        # O(n)
class Solution1:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        dict={}
        
        for x in num:
            dict[x] = 1
            
        ans = 0
        
        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1 
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len
                    
        return ans


# O(nlogn)
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        l = num[0] 
        ans = 1
        tmp = 1
        print("num is ",num)
        for n in num:
            print("n is ",n, "l is ",l)
            if(n - l == 0):
                continue;
            elif(n - l == 1):
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
            l = n
        if tmp > ans:
            ans = tmp
        return ans
      


mySol = Solution()
print("data is ", data)
res = mySol.longestConsecutive(data)        
print("res is ", res)