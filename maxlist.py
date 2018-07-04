class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        print("dp is ",dp)
        return max(dp)
import sys
class Solution2:
    '''
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
    '''
    def longestIncreasingSubsequence(self,nums):
        length = len(nums)
        maxdata=9999
        minLast = [maxdata]*(1+length);
        minLast[0] = -maxdata-1;

        
        for i in range(0, length):
            #// find the first number in minLast >= nums[i]
            index = self.binarySearch(minLast, nums[i]);
            minLast[index] = nums[i];
            print(i, nums[i],index)
            print(minLast)
        
        print("minlast", minLast)        
        for i in range(length, 0, -1):
            if (minLast[i] != maxdata) :
                return i;
            
        

        return 0;
    
    
    # find the first number > num
    def  binarySearch(self,minLast, num):
        start = 0; end = len(minLast) - 1;
        while (start + 1 < end):
            mid = int((end - start) / 2 + start);
            if (minLast[mid] < num):
                start = mid;
            else:
                end = mid;
        return end;
data= [1,3,2,-1,99,2]


mysolution = Solution() 
#res = mysolution.longestIncreasingSubsequence(data)       
#print(res)


print("solution2-----------------------------")
print("data", data)    
mysolution2 = Solution2() 
res = mysolution2.longestIncreasingSubsequence(data)       
print(res)