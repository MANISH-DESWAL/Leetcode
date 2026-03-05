#Quick sort an array
#Time Cmplecity: O(nlog(n)) for avg and best case and O(n**2) for worst case
#Space Complexity: O(log(n)) for avg and best case and O(n) for worst case

class Solution:
    def partition(self,nums,l,r):

        '''this patition function is used to find the "key" that seperate the list
        in two parts left will smaller then key and right will greater'''

        #let key is r(last element)
        #start will update values according to key 
        key =nums[r]
        start =l
        
        for i in range (l,r):
            print(f"start={start} key={key} and i,nums[i]={i,nums[i]}")
            if nums[i]<=key:
                temp=nums[i]
                nums[i]=nums[start]
                nums[start]=temp
                start+=1
        # CHANGE: Move the key into its correct spot
        nums[start], nums[r] = nums[r], nums[start]
        
        return start                 #as we can see at start increased to one from thatkey value
    
    def quick_sort(self,nums,l,r):
        '''In quick sort we make patiions in two arrays one has smakker or eqial values to key
        other one will have largers'''
        #base  case 
        if l>=r:
            return
        #Recursive case 
        
        p=self.partition(nums,l,r)
        print(p)
        self.quick_sort(nums,l,p-1)
        self.quick_sort(nums,p+1,r)

    def sortArray(self, nums: List[int]) -> List[int]:
        
        # def Quick_sort(self,nums,l,r ):
        self.quick_sort(nums,0,len(nums)-1)
        return nums

a=Solution()
print(a.sortArray([3,2,6,5,4,10,3,1,8,11,8,9,7,6]))

    





     
