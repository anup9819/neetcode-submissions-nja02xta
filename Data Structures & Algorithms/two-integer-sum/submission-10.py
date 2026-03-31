class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        rem_dic = {}
        while(i<len(nums)):
            reminder = target-nums[i]
            if reminder not in rem_dic:
                rem_dic[nums[i]]=i
            else:
                return [rem_dic[reminder],i]
            i+=1
                
        