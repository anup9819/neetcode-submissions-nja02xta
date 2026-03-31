class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[]for i in range(len(nums)+1)]
        my_dic = {}
        result = []
        for i in nums:
            my_dic[i] = my_dic.get(i,0)+1

        for key,value in my_dic.items():
            res[value].append(key)

        for i in range(len(res)-1,0,-1):
            for v in res[i]:
                result.append(v)
                if len(result)==k:
                    return result
            