class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, bs = [],[]
        def rec_bac(openn,closen):
            if openn == closen == n:
                bs.append("".join(ans))
                return
            
            if openn < n:
                ans.append("(")
                rec_bac(openn+1,closen)
                ans.pop()
            if closen<openn:
                ans.append(")")
                rec_bac(openn,closen+1)
                ans.pop()
        rec_bac(0,0)
        return bs

