class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=0
        right=n-1
        i=0
        while i<=right:
            print(f"left,i,right == {left,i,right} and nums[left],nums[i],nums[right] == {nums[left],nums[i],nums[right]} and nums={nums}")
            if nums[i]==0:
                temp=nums[left]
                nums[left]=nums[i]
                nums[i]=temp
                # i+=1
                left+=1
                i+=1
            elif nums[i]==2:
                temp=nums[i]
                nums[i]=nums[right]
                nums[right]=temp
                # i+=1
                right-=1
            else:
                i+=1
        return nums


a=Solution()
print(a.sortColors([2,0,1]))