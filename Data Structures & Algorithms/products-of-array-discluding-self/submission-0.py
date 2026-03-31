class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_arr = [0]*len(nums)

        prefix_val = 1
        for i in range(len(nums)):
            res_arr[i] = prefix_val
            prefix_val*=nums[i]
        postfix_val = 1
        for i in range(len(nums)-1,-1,-1):
            res_arr[i]*=postfix_val
            postfix_val*=nums[i]
        return res_arr
