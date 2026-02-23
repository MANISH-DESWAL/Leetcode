class Solution:
    def s_sort(self,s):
            s=[i for i in s]
            s.sort()
            return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        dict2={}
        a=0
        for i in strs:
                key=self.s_sort(i)
                if key in dict:
                      dict[key].append(i)
                      
                else:
                      dict[key]=[i]
        return list(dict.values())


        
        
            

a=Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
