class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      

        for i in range(0, len(nums)):
            rem = target - nums[i]
            
            
            if rem in nums[i+1:len(nums)]:
                id =  nums[i+1:len(nums)].index(rem)
                return [i,i+id+1]
        


     