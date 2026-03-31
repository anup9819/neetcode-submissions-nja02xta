class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_arr = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res_arr[i]=prefix
            prefix*=nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res_arr[i]*=postfix
            postfix*=nums[i]
        return res_arr
            
        