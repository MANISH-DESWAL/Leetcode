class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                L1=[]
                s=set()
                

                for i in range(len(nums)):
                    for j in range(i+1,len(nums)):
                        for k in range(j+1,len(nums)):
                            if nums[i]+nums[j]+nums[k]==0:
                                    tri= tuple(sorted([nums[i],nums[j],nums[k]]))
                                    
                                    s.add(tri)
                                    
                L1=[list(t) for t in s]
            
                return L1
        
a=Solution()
print(a.threeSum([12,6,-18,5,6]))



