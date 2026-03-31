class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                continue
            if nums[k]>0:
                break
            
            pivot = nums[k]
            i,j = k+1,len(nums)-1
            while(i<j):
                if pivot+nums[i]+nums[j]==0:
                    res.append([pivot,nums[i],nums[j]])
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif pivot+nums[i]+nums[j]<0:
                    i+=1
                else:
                    j-=1
        return res