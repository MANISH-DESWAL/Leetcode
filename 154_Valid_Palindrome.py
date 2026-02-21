class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="qwertyuiopasdfghjklzxcvbnm1234567890"
        s=s.lower()
        i=0
        j=len(s)-1
        
        while j >= i:
            if s[j] in a and s[i] in a:
                # print(s[i],s[j])
                if s[i]==s[j]:

                    i+=1
                    j-=1
                    if j<i:
                        return True


                else:

                    return False
            
            elif s[i] not in a:
                # print(f"s[i]=={s[i]}")
                i+=1
                if j<i:
                        
                        return True
                
            elif s[j] not in a:
                # print(f"s[j]== {s[j]}")
                j-=1
                if j<i:
                        return True
             

            

a=Solution() 
print(a.isPalindrome("0P"))