class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dic = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in result_dic:
                result_dic[nums[i]]=i
            else:
                return [result_dic[rem],i]
        return False