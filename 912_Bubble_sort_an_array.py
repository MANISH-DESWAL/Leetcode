#bubble Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        l=len(nums)
        isswap=False
        for i in range(0,len(nums)-1):
            for j in range (len(nums)-i-1):
                # print(f"i,j={i,j} & nums[j]={nums[j]} and j+1={nums[j+1]}")
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                    isswap=True
        return nums

a=Solution()
print(a.sortArray([1,2,6,5,4,10,3,7,8,9]))