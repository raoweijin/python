class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
    def partitionArray(self, nums, k):
        start, end = 0, len(nums)-1
        while start < end:
            if nums[start]
    
data = [ 2,3,9,10,1,6]
k = 5
print("data is ",data)
print("k is ",k)
mySol = Solution()
res = mySol.partitionArray(data,k)

print("res is ",res)
print("data is ",data)