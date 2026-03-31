class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        i, j = 0,0
        max_len = 0
        while(j<len(s)):
            if s[j] not in seen:
                seen.append(s[j])
                j+=1
            else:
                seen.pop(0)
                i+=1
            max_len = max(max_len,len(seen))
        return max_len