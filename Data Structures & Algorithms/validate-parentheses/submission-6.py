class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        result_list = []
        for i in s:
            if i in dic.keys():
                result_list.append(i)
            elif len(result_list)==0 or i!=dic[result_list.pop()]:
                return False
        return len(result_list)==0
                