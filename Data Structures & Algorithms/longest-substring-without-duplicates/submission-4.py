class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        i,j =0,0
        while(j<len(s)):
            if s[j] not in char_set:
                char_set.add(s[j])
                j+=1
                max_len=max(max_len,j-i)
            else:
                char_set.remove(s[i])
                i+=1
        return max_len
        