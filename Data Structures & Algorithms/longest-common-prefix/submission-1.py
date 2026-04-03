class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        for i in range(len(pivot)):
            for s in strs[1:]:
                if i==len(s) or pivot[i]!=s[i]:
                    return pivot[:i]
        return pivot
        