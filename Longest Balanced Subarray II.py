class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        l1=nums
        o=0
        e=0
        l2=[0]
        l3=[]
        
        
          
        for i in range(0,len(l1)-1):
            j=i+1
            if (l1[i]%2==0 and l1[j]%2!=0) or (l1[i]%2!=0 and l1[j]%2==0) :
                
                o += 1
                e+=1
                print(l1[i],l1[j],"       ",o,e)
                l3.append(l1[i])
                l3.append(l1[j])
            elif l1[j] in l3:
                if l1[j]%2==0:
                    e+=1
                else:
                    o+=1    
            else:
                l2.append(o)
                l2.append(e)
                o,e=0
            if o<=e:
                l2.append(o) 
            else:   
                l2.append(e) 

            

                
            i+=1 
        return l2,max(l2)+1

a=Solution()
print(a.longestBalanced([1,2,3,2]))