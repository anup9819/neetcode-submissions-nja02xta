class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dic to count the element and use frequency array where index will be the time of occurences and element will be sorted to the freq. index
        counter_dic = {}
        fre_array = [[] for i in range(len(nums)+1)]
        result = []
        # this is counting the number of times a element has occured via dictonary as we always do
        for i in nums:
            counter_dic[i] = counter_dic.get(i,0)+1
            
        #now we are going to shift these items and count to the fre_array whihc is 2d array every index and a seperate array to hold multiple values for a same index
        # v here which is number of times a element has appeared will be the key as they are indexes
        for key,value in counter_dic.items():
            fre_array[value].append(key)
            
        #here we put element traversing back from the freq. array as we need most frequent element and as index was indicating the same then the last index means that much time
        #of occurnace of an an element 0,1,2,3,4 then last element has seen to be appeared 4 times
        for i in range(len(fre_array)-1,0,-1):
            #we go to the index and then we have array under than index right so one more loop to get the elements from that array
            for n in fre_array[i]:
                result.append(n)
                if len(result)==k:
                    return result