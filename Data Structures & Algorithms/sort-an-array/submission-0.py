class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <=1:
            return nums

        x = len(nums)-1
        while x != 0:
            j = 0;
            while j<x:
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j]= nums[j], nums[j+1]
                j +=1
            x -= 1
        
        return nums