from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile =  max(piles)
        #min_banana = float('inf')
        low, high  = 1, max_pile
        while(low<=high):
            temp = 0
            mid = (low+high)//2
            for i in piles: 
                temp+= ceil(i/mid)
            if temp>h:
                low=mid+1
                #min_banana=min(min_banana,mid)
            else:
                high =mid-1
        return low