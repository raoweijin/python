'''
544. Top k Largest Numbers 
 Description
 Notes
 Testcase
 Judge
Given an integer array, find the top k largest numbers in it.

Have you met this question in a real interview? 
Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].


class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        
'''        
        
import heapq

class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)
        
    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num)
        elif num > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, num)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        # Write your code here
        print("nums is ", self.nums)
        return sorted(self.nums, reverse=True)
data = [3,10,1000,-99,4,100]
print("data is ",data)
k =3
mySolu = Solution(k)
for ie in data:
    mySolu.add(ie)
res = mySolu.topk()
print("res is ", res)