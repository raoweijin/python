import copy
class solution:
    def target(self, nums, target):       
       # Write your code here
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        data=[[[]]]*(target+1)
        for a in nums:
            for j in range(target, a - 1, -1):               
                dp[j] += dp[j - a]
                if(0 != dp[j-a]):
                    print(j,j-a,a)
                    temp = copy.deepcopy(data[j])
                    temp2 = copy.deepcopy(data[j-a])
                    for element in temp2:
                        element = element + [a]
                    data[j]= copy.deepcopy(temp.append(temp2))
            print("data: ", data)
        print(dp)
        print(data)
        return dp[target]
        

mysolution = solution()
nums= [1,2,3,3,7]
target = 7
print(nums)
print(target)
result = mysolution.target(nums, target)
print(result)     