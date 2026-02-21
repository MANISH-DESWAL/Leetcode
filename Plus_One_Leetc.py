class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #here we firstly converted list into str then int and added +1 
        num=int("".join(map(str,digits))) + 1
        return list(map(int,str(num))) #converted back to a list

a=Solution()   
print(a.plusOne([9,9,9,9])) 