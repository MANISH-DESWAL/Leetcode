class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            if len(s)==1:
                if s==t:
                    return True
                else:
                    return False
            else:
                dict1={}
                dict2={}
                for i in s:
                    if i in dict1 :
                        dict1[i]+=1
                    else:
                        dict1[i]=1
                for i in t:
                    if i in dict2:
                        dict2[i]+=1
                    else:
                        dict2[i]=1
                if dict1==dict2:
                    return True
                else:
                    return False




a=Solution()
print(a.isAnagram("anagram","nagaram"))
 