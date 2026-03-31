class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dic = {}
        for i in range(len(nums)):
            if i not in dic:
                dic[nums[i]]=i
        def binary_search(arr):
            if not arr:
                return -1
            mid = len(arr)//2
            if arr[mid]== target:
                return dic[arr[mid]]
                
            if arr[mid]>target:
                return binary_search(arr[0:mid])
            else:
                return binary_search(arr[mid+1:])
        return binary_search(nums)