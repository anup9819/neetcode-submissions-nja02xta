class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp=nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i]==temp:
                count+=1
            elif nums[i]!=temp and count>=1:
                count-=1
            elif count<=0 and nums[i]!=temp:
                temp = nums[i]
                count=1
        return temp