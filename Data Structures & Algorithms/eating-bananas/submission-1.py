from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high  = 1, max(piles)
        while(low<=high):
            temp = 0
            mid = (low+high)//2
            for i in piles: 
                temp+= ceil(i/mid)
            if temp>h:
                low=mid+1
            else:
                high =mid-1
        return low