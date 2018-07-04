class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        hs = {0:-1}
        sum = 0
        for i in range(len(nums)):
            # if A[i] == 0:
            #     return [i, i]
            sum += nums[i]
            if sum in hs:
                return [hs[sum] + 1, i]
            hs[sum] = i
            print("hs is ",hs,"i is ",i,"sum is ",sum)
        return 
data = [9,-3, 1, 2, -3, 4]
print("data is ",data)
mySolution = Solution()
res = mySolution.subarraySum(data)
print("res is ",res)
'''        
        
        public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    public ArrayList<Integer> subarraySum(int[] nums) {
        // write your code here
       
        int len = nums.length;
       
        ArrayList<Integer> ans = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
       
        map.put(0, -1);
       
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += nums[i];
           
            if (map.containsKey(sum)) {
                ans.add(map.get(sum) + 1);
                ans.add(i);
                return ans;
            }
            
            map.put(sum, i);
        }
       
        return ans;
    }
}
'''