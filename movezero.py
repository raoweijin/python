a = [1,0,0,0,2,0,0,3,0]
print(a)
'''
start = 0
end = 0
length= len(a)
while(end<length):
    if(a[end]!=0):
        swap(a[start],a[end])
        start+=1
    end+=1
'''
class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes2(self, nums):
        start = -1
        switchFlag = False
        length = len(nums)
        for i in range(length):
            if nums[i] != 0 and switchFlag:
                nums[start], nums[i] = nums[i],nums[start]
                switchFlag = False
            if nums[i] == 0 and switchFlag == False:
                switchFlag = True
                start = i          
    def moveZeroes3(self, nums):
        start = 0; end = 0
        switchFlag = False
        length = len(nums)

        while start < length and end < length:
            print("start is ",start, " end is ",end)
            if nums[start] != 0:
                start+=1  
                end = start+1 
            else:
                if nums[end] ==0:
                    end+=1
                else:
                    nums[start], nums[end] = nums[end],nums[start]
                    start+=1
                    end = end+1
    
    
    def moveZeroes(self, nums):
        # Write your code here
        left = 0;
        right = 0;
        while right < len(nums):
            if nums[right] != 0:
                if(left!=right):                
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1;
                print("hi")
            right += 1;
            print(nums)

mySolution = Solution()      

mySolution.moveZeroes3(a)      

print(a)
    
    
    
    
    
    
    