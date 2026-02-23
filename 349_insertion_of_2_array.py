class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # uni=[]
        # for i in nums1:
        #     print(i)
        #     if i in nums2 :
        #         uni.append(i)
        # return uni 

        #2nd way -
        
        # s1=set(nums1)
        # s2=set(nums2)
        return list(set(nums1)&set(nums2))
a=Solution()
print(a.intersection([1,2,2,1],[2,2]))        