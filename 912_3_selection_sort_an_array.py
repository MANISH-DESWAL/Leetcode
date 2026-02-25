#selection sorting

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n-1):
            smallest=[nums[i],i]
            

            for j in range(i,n):
                if nums[j]<smallest[0]:
                    smallest[0]=nums[j]
                    smallest[1]=j
            nums[smallest[1]]=nums[i]
            nums[i]=smallest[0]        
                
        return nums
                                                                                                                                                                                                                                                                                                                                                                                                