#Merge Sort
#here We mainly focus on sorting with recursive algo.
#It has O(n**2) TC for all cases and space complexity O(1)
class Solution:
    def merge(self,nums,l,mid,r):
        
        #a = first subarray (l to mid)
        #b = second sub array (mid to r))
        a=[]
        b=[]

        for i in nums[l:mid+1]:
            a.append(i)
        for i in nums[mid+1:r+1]:
            b.append(i)
        print(f"l={l},mid={mid},r={r} and a={a},b={b} and ")
        
        i=0
        k=l
        j=0
        while k<=r:
            if i>len(a)-1:
                nums[k]=b[j]
                j+=1
                k+=1
            elif j>len(b)-1:
                nums[k]=a[i]
                i+=1
                k+=1

            elif a[i]<b[j]:
                nums[k]=a[i]
                i+=1
                k+=1
            else:
                nums[k]=b[j]
                j+=1
                k+=1
        return
            



        
    def merge_sort(self,nums,l,r):
        
        # recursive case:--
        if l<r:
        
            mid =(l+r)//2
            print(f"l={l},r={r},mid={mid}")

            # from l to mid
            
            self.merge_sort(nums,l,mid)
            #from mid to r
            self.merge_sort(nums,mid+1,r)
            
            self.merge(nums,l,mid,r)
        else:
            return

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)
        return nums


a=Solution()
print(a.sortArray([11,2,6,5,4,10,3,7,8,9,1]))