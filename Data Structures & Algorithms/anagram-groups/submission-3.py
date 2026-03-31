from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect_dict = defaultdict(list)
        for word in strs:
            key = [0]*256
            for i in word:
                key[ord(i)-ord("a")]+=1
            collect_dict[tuple(key)].append(word)
        return list(collect_dict.values())
