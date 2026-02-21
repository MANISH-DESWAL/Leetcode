# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final_list=[]
        for i in lists:
            final_list.extend(i)

        
        
        final_list.sort()
        return final_list


a=Solution()
print(a.mergeKLists([[1,2,3,4],[3,4,5,6]]))

        