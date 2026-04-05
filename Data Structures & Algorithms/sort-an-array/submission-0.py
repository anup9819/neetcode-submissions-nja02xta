class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,L,M,R):
            left_arr,right_arr = arr[L:M+1],arr[M+1:R+1]
            i,j,k=L,0,0
            
            while (j<len(left_arr) and k<len(right_arr)):
                if left_arr[j]<right_arr[k]:
                    arr[i]=left_arr[j]
                    j+=1
                else:
                    arr[i]=right_arr[k]
                    k+=1
                i+=1
            while(j<len(left_arr)):
                nums[i]=left_arr[j]
                j+=1
                i+=1
            while(k<len(right_arr)):
                nums[i]=right_arr[k]
                k+=1
                i+=1
                

        def merge_sort(arr,l,r):
            if l==r:
                return arr
            mid = (l+r)//2
            merge_sort(arr,l,mid)
            merge_sort(arr,mid+1,r)
            merge(arr,l,mid,r)
            return  arr
        return merge_sort(nums,0,len(nums)-1)