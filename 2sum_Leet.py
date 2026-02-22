# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i=0
#         j=1
#         l1=[]
#         while nums[i]+nums[j]!=target and i!= len(nums)-1:
#             j=j+1
#             if j==len(nums):
#                 i+=1
#                 j=i+1
#         else :
#             l1.append(i)
#             l1.append(j)

#             return l1    
        

        #2nd way:--
class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                dict={}
                for i in range(0,len(nums)):
                    # print(f"dict[target-nums[i]]={dict[target-nums[i]]},i={i}")
                    if target-nums[i]  in dict.keys():
                        print(f"dict[target-nums[i]]={dict[target-nums[i]]},i={i}")
                        return [dict[target-nums[i]],i]
                    
                    else:
                        
                        dict[nums[i]]=i
                        print(f"dict[target-nums[{i}]]={dict[nums[i]]},target-nums={target-nums[i]}")
            

a=Solution()
print(a.twoSum([3,2,4],6))
