class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1=""
        j=0
        i=0
        if strs[i]!= "":   
            if len(strs)>1:   
                while i != (len(strs)):
                        if i > (len(strs)-1):
                            str1=str(str1+str(strs[i][j]))
                            i=0 
                            j+=1
                        else    :
                            if j> (len(strs)-1 ):
                                break
                            else:   
                                if strs[i][j]!=strs[i+1][j]:
                                    break
                                else:
                                    i+=1
            elif len(strs)==1:
                str1=str1+str(strs[0])
        return str1,type(str1),str(strs[0])
print(Solution().longestCommonPrefix([["apple","appee"]]))    