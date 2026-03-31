class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_array = [[] for i in range(len(nums) + 1)]
        dic = {}
        res = []
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key,value in dic.items():
            freq_array[value].append(key)
        for i in range(len(freq_array)-1,0,-1):
            for n in freq_array[i]:
                res.append(n)
                if len(res)==k:
                    return res
            