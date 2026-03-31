class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(i for i in nums)
        return len(res)!=len(nums)
        