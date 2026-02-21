class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            
                i = 0
                j = 0
                n3 = []

                # compare while both pointers are valid
                while i < len(nums1) and j < len(nums2):
                    if nums1[i] < nums2[j]:
                        n3.append(nums1[i])
                        i += 1
                    else:
                        n3.append(nums2[j])
                        j += 1

                # add remaining elements from nums1
                while i < len(nums1):
                    n3.append(nums1[i])
                    i += 1

                # add remaining elements from nums2
                while j < len(nums2):
                    n3.append(nums2[j])
                    j += 1

            
                if 0 <= len(nums1) <= 1000 and 0 <= len(nums2) <= 1000 and 1 <= len(nums1) + len(nums2) <= 2000 :
                    
                    if len(n3)%2==0:
                        return (n3[(int(len(n3)/2) -1)]+n3[(int(len(n3)/2))])/2
                    
                    else:
                         return(n3[int(((len(n3)+1)/2-1))])
    


        
        

b=Solution()
print(b.findMedianSortedArrays([1,3],[2,3,4,5,6,7,8]))            
                
