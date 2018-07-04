

def maxSum2(data):
    maxSum = -999
    sum = 0; minSum = 0;
    length = len(data)
    for ie in data:
        sum += ie
        maxSum = max(sum-minSum,maxSum)
        minSum = min(minSum,sum)
        print("maxSum is ",maxSum, " minSum is ",minSum, " sum is ",sum)
    return maxSum       

    
'''
public class Solution {
    public int maxSubArray(int[] A) {
        if (A == null || A.length == 0){
            return 0;
        }
        
        int max = Integer.MIN_VALUE, sum = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            max = Math.max(max, sum);
            sum = Math.max(sum, 0);
        }

        return max;
    }
}
'''
data= [-1,9,-100,1,3,4,3,-900]
print("data is ",data)
def maxSum(data):
    maxSum = -9999
    sum = 0
    length = len(data)
    for i in range(length):
        sum += data[i]
        maxSum = max(maxSum,sum)
        sum  = max(sum,0)
    return maxSum
res = maxSum(data)
print("res is ", res)

res2 = maxSum2(data)
print("res2 is ", res2)