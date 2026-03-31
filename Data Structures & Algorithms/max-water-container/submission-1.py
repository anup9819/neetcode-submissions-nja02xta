class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result_container = 0
        i,j = 0, len(heights)-1
        while(i<j):
            min_height = min(heights[i],heights[j])
            volume = min_height*(j-i)
            if volume>result_container:
                result_container = volume
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return result_container
        