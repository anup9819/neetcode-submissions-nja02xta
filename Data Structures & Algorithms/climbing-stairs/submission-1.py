class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {0:1,1:1}
        for i in range(2,n+1):
            dic[i]=dic[i-1]+dic[i-2]
        return dic[n]