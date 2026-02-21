class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        def sum(lst):
            temp=0
            for i in lst:
                temp+=i
            return temp
        newl=[]
        if len(accounts)==1:
            newl.append(sum(accounts[0]))

        else:    
            for i in range(0,len(accounts)-1):
                newl.append(sum(accounts[i]))
        return max(newl)  
a=Solution()
print(a.maximumWealth([[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]
))    