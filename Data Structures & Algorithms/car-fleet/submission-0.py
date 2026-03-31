class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_arr = [[p,s] for p,s in zip(position,speed)]
        stk = []

        for p,s in sorted(pair_arr)[::-1]: #this is sorted and traversing in reverse
            stk.append((target-p)/s)
            while len(stk)>=2 and stk[-2]>=stk[-1]:
                stk.pop()
        return len(stk)
        