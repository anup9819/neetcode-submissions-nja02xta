class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        
        #leftmax array
        leftmax[0]=height[0]
        for i in range(1,len(height)):
            leftmax[i] = max(leftmax[i-1],height[i])
        
        #rightmax array
        rightmax[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightmax[i] = max(rightmax[i+1],height[i])

        #final 
        total_water = 0
        for i in range(len(height)):
            total_water+=min(leftmax[i],rightmax[i])-height[i]
        return total_water


        