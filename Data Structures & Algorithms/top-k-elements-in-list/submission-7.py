class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for i in range(len(nums)+1) ]
        my_dict = {}
        res = []
        for i in nums:
            my_dict[i] = my_dict.get(i,0)+1

        for key,value in my_dict.items():
            freq_arr[value].append(key)

        for i in range(len(freq_arr)-1,0,-1):
            for n in freq_arr[i]:
                res.append(n)
                if len(res)==k:
                    return res