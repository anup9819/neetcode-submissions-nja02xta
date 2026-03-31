class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")","[":"]","{":"}"}
        stack = []
        for i in s:
            if i in dic:
                stack.append(dic[i])
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0