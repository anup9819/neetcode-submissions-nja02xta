class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dic_result(s):
            result_dic = {}
            for i in range(len(s)):
                if s[i] not in result_dic:
                    result_dic[s[i]]=1
                else:
                    result_dic[s[i]]+=1
            return result_dic
        return dic_result(s)==dic_result(t)

        