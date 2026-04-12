class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        counter = 0
        static="+DC"
        for i in operations:
            if i not in static:
                stk.append(int(i))
            elif len(stk)>1 and i == "+":
                val1,val2 = stk[-1],stk[-2]
                stk.append(val1+val2)
            elif i=="C":
                stk.pop()
            elif len(stk)>=1 and i=="D":
                stk.append(stk[-1]*2)
        for i in stk:
            counter+=i
        return counter