class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def To_dict(s):
            dict = {}
            for i in s:
                dict[i] = dict.get(i,0)+1
            return dict
        return To_dict(s)==To_dict(t)
        