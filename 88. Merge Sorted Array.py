class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m=len(nums1)
        # n=len(nums2)
        i=m-1
        j=m+n-1 
        k=n-1
        # if n==0:
        #     pass
        # elif m==0:
        #     for i in range (len(nums1)):
        #         nums1[i]=nums2[i]
        # else:
        while j>=0:
                # print(f"{nums1,nums2} and val of i,j,k ={nums1[i],nums1[j],nums2[k]} and i,j,k are {i,j,k} m,n={m,n}")
                if nums2[k]>nums1[i]:
                    # temp=nums2[k]
                    # nums2[k]=nums1[j]
                    nums1[j]=nums2[k]
                    k-=1
                    j-=1
                # elif i<0:
                #     if k<0:
                #         pass
                #     else:
                #         for j in ra   nge(0,k+1):
                #             nums1[j]=nums2[j]
                #     break
                else:
                    # temp=nums1[i]
                    nums1[j]=nums1[i]
                    
                    k-=1
                    i-=1
                

                    
                    
        # print(f"{nums1,nums2} and val of i,j,k ={nums1[i],nums1[j],nums2[k]} and i,j,k are {i,j,k}")



        
        return nums1
                    



            
a=Solution()
print(a.merge([2,0],1,[1],1))