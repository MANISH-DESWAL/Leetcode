class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i=dividend
        div=divisor
        count=0
        if i<0 or div<0: 
            if (0-i)==div or i==(0-div):
                count=-1
            elif i<0 and div>0:
                i=0-i
                while i>divisor:
                    i=i-divisor
                    count-=1

            elif i>0 and div<0:
                div=0-div
                while i>div:
                    i=i-div
                    count=count-1
                    # return i,div,count
                  

            else:
                i=0-i
                div=0-div
                if i==div :
                    count=1
                else:
                    while i>div:
                        i=i-div
                        count-=1

                    
        else:    
            if i==div :
                count=1
                
            else:    
                while i>divisor:
                    i=i-divisor
                    count+=1
        return count    

a=Solution()
print(a.divide(7,-3))    

        
        