class Solution:
    def firstUniqChar(self, s: str) -> int:
        a={}
        b=0
        for i in s:
            if i not in a:
                a[i]=1

            else:
                a[i]+=1
        
        for i in a.keys():
            if a[i]==1:
                return s.index(i)
            

        return -1
    
                  


a=Solution()
print(a.firstUniqChar("love"))