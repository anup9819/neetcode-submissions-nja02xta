class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = temperatures
        res_arr = [0]*len(n)
        stk = []
        stk.append(len(n)-1)
        for i in range(len(n)-1,-1,-1):
            while stk and n[i]>=n[stk[-1]]:
                stk.pop()
            if stk:
                res_arr[i]=stk[-1]-i
            stk.append(i)
            
        return res_arr
        