class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        i=0
        j=len(s)-1
        while j>i:
            temp=s[j]
            s[j]=s[i]
            s[i]=temp
            j-=1
            i+=1
        return s    
        