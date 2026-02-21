class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=1
        l1=[]
        while nums[i]+nums[j]!=target and i!= len(nums)-1:
            j=j+1
            if j==len(nums):
                i+=1
                j=i+1
        else :
            l1.append(i)
            l1.append(j)

            return l1    
            

a=Solution()
print(a.twoSum([1,2,3,5,6],11))
