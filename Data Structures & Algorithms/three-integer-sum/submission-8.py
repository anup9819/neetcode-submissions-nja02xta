class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for p in range(len(nums)-2):
            i,j = p+1,len(nums)-1
            if p>0 and nums[p]==nums[p-1]:
                continue
            if nums[p]>0:
                break
            while(i<j):
                if nums[p]+nums[i]+nums[j]==0:
                    res.append([nums[p],nums[i],nums[j]])
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif nums[p]+nums[i]+nums[j]<0:
                    i+=1
                else:
                    j-=1
        return res