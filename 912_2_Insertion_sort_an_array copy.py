#insertion Sort
#TC - O(n**2) for all TCs and O(1) SC
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while nums[j]>key and j>=0:
                nums[i]=nums[j]
                nums[j]=key
                j-=1
                i-=1
            
        return nums

a=Solution()
print(a.sortArray([3,2,6,5,4,10,3,1,7,8,9]))