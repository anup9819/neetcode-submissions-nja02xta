class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        res_str = ""
        while l<len(word1) and r<len(word2):
            res_str+=word1[l]+word2[r]
            l+=1
            r+=1
        while l<len(word1):
            res_str+=word1[l]
            l+=1
        while r<len(word2):
            res_str+=word2[r]
            r+=1
        return res_str


        