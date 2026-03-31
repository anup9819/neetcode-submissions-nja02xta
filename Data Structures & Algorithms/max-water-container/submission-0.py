class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        start, end = 0,len(heights)-1
        while(start<end):
            less_val = min(heights[start],heights[end])
            if less_val*(end-start)>max_val:
                max_val = less_val*(end-start)
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        return max_val