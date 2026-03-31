class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = [0]*(len(nums)*2)
        for i in range(len(nums)):
            l[i]=nums[i]
            l[len(nums)+i]=nums[i]
        return l

        