class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_logic(arr,l,r,Target):
            if l>=r:
                return -1
            m=l+(r-l)//2
            if Target == arr[m]:
                return m
            elif Target<arr[m]:
                return binary_logic(arr,l,m,Target)
            else:
                return binary_logic(arr,m+1,r,Target)
        return binary_logic(nums,0,len(nums),target)
