class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dicify(s):
            dic ={}
            for i in s:
                dic[i] = dic.get(i,0)+1
            return dic 

        return dicify(s) == dicify(t) 
        