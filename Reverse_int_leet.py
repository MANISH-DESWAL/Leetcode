class Solution:
    def reverse(self, x: int) -> int:
        new_x=""
        str_x=str(x)
        for i in range(len(str_x)-1,-1,-1):
            new_x+=str_x[i]

        return new_x
        
 
a=Solution()
print(a.reverse(1534236469))
