'''
Counting sort is fast just it take the O(n) SC
and TC for it is O(n+k)
Here we take an other array let b which has - (the length max of given array let a) +1
which has zero values in it 
for every iterationn in a we increase the index value(where a value is ) of b by one

'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mx =max(nums)
        l1=[0]*(mx+1)
        
        for i in nums :
            l1[i]+=1
        nums=[]
        for i in range(0,len(l1)):
            while l1[i]>0:
                nums.append(i)
                l1[i]-=1
        return nums

                

a=Solution()
print(a.sortArray([3,2,6,5,4,10,3,1,8,11,8,9,7,6])) 
