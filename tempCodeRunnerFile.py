#bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        l=len(nums)
        isswap=False
        for i in range(0,len(nums)-2):
            for j in range (i,len(nums)):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    isswap=True
            
            if isswap==False:
                break