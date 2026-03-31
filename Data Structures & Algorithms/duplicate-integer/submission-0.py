class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        coll = set()
        for i in nums:
            if i in coll:
                return True
            else:
                coll.add(i)
        return False
        