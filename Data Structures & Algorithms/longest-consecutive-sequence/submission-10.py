class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hash_set = set(nums)
        max_counter = 1
        for i in nums:
            start = i
            counter = 1
            if i-1 not in hash_set:
                while start+1 in hash_set:
                    start+=1
                    counter +=1
                    max_counter = max(max_counter,counter)
        return max_counter
            
                    