class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}
        res = []
        index_arr = [[] for i in range(len(nums)+1)]
        for i in nums:
            freq_dic[i] = freq_dic.get(i,0)+1

        for key,value in freq_dic.items():
            index_arr[value].append(key)

        for i in range(len(index_arr)-1,-1,-1):
            for n in index_arr[i]:
                res.append(n)
                if len(res)==k:
                    return res