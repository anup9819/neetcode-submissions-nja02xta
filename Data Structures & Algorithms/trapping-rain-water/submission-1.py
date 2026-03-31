class Solution:
    def trap(self, height: List[int]) -> int:
        res_water = 0
        l_max = []
        l_max.append(height[0])
        for i in range(1,len(height)):
            l_max.append(max(l_max[i-1],height[i]))
        r_max = [0]*len(height)
        r_max[-1]=height[-1]
        for j in range(len(height)-2,-1,-1):
            r_max[j]=max(r_max[j+1],height[j])
        for i in range(len(height)):
            res_water+=min(l_max[i],r_max[i])-height[i]

        return res_water