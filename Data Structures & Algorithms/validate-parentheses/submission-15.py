class Solution:
    def isValid(self, s: str) -> bool:
        para_dic = {
            "}":'{',
            "]":"[",
            ")":"("
        }
        container = []
        for i in s:
            if i in para_dic and container==[]:
                return False
            if i in para_dic:
                if para_dic[i]!=container.pop():
                    return False
            else:
                container.append(i)

        return len(container)==0