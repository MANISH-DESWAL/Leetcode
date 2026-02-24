class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        mega="abcdefghijklmnopqrstuvwxyz"
        l1=[]
        count=0
        for i in range(0,len(s)-2):
            l1.append(s[i:i+3])
        for i in l1:
            st=set(i)
            
            if len(st) ==3:
                count+=1
        return count,l1

a=Solution()
print(a.countGoodSubstrings("owuxoelszb"))