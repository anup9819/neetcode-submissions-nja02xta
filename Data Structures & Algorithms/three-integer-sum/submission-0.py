class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = sorted(nums)
        ans_lis = []
        for ind in range(len(num_set)):
            i,j = ind+1,len(num_set)-1
            while(i<j):
                if num_set[ind]+num_set[i]+num_set[j]==0:
                    if [num_set[ind],num_set[i],num_set[j]] not in ans_lis:
                        ans_lis.append([num_set[ind],num_set[i],num_set[j]])
                if num_set[ind]+num_set[i]+num_set[j]>0:
                    j-=1
                else:
                    i+=1
        return ans_lis