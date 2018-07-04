class solution:
    def target(self, nums, target):
        nums.sort()
        length = len(nums)
        status = [0]*(target+1)
        status[0] =1
        for i in range(1, target+1):
            for j in range(0, length):

                pre = i - nums[j]
                if(pre >= 0):
                    if( pre <= round(i/2)):
                        status[i] += status[pre]
                        status[i] = status[i]-(nums[j]== pre)
        print(status)
        return status[target]    

mysolution = solution()
nums= [1,2,3,3,7]
target = 7
print(nums)
print(target)
result = mysolution.target(nums, target)
print(result)