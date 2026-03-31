class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        res = []
        for i in s:
            if i in dic:
                if res and res[-1] == dic[i]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        return len(res)==0

            
            