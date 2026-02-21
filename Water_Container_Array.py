class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        i=0
        j=1
        def area(a,b,h):
            if h[a]<h[b]:
                return h[a]*(b-a)
            else:
                return h[b]*(b-a)

        if len(height)>2:        
            while i != (len(height)-2):
                if j==len(height):
                    i=i+1
                    j=i+1
                m=  area(i,j,height)  
                if m>=max_area:
                    max_area=m
                j=j+1   
        elif len(height)==2:
            if height[i]<height[j]:
                max_area=( height[i]*(j-i))
            else:
                max_area=( height[j]*(j-i))

        return max_area    

a=Solution()
print(a.maxArea([2,4,9,9]))
            


        