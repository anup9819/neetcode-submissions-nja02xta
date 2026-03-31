class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        lis = []
        for i in nums:
            dic[i] = dic.get(i,0)+1       
        key = list(dic.keys())
        Value = list(dic.values())
        for i in range(k):
              inde = Value.index(max(Value))
              print(inde)
              lis.append(key[inde])
              Value[inde]=0
        return lis
                    