class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= defaultdict(list)
        for word in strs:
            dic_key = [0]*26
            for i in word:
                dic_key[ord(i)-ord("a")]+=1
            result[tuple(dic_key)].append(word)
        return list(result.values())
        