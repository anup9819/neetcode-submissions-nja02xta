class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest=0
        for i in new_set:
            if i-1 not in new_set:
                length = 1
                while(i+length in new_set):
                    length+=1
                longest=max(length, longest)
        return longest
