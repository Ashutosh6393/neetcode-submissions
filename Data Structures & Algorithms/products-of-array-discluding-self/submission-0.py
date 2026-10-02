class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = []

        j = len(nums) -1

        l = 1
        r = 1
    
        for n in nums:
            l = l * n
            left.append(l) 

            r = r * nums[j]
            right.append(r)

            j -= 1
        
        right.reverse()

        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(right[i+1])
            elif i == len(nums)-1:
                result.append(left[i-1])
            else:
                result.append(left[i-1] * right[i+1])

        
        return result



        