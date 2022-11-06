# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=outPut=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                outPut.next=list1
                list1,outPut=list1.next,list1

            else:
                outPut.next=list2
                list2,outPut=list2.next,list2

        if list1 or list2:
            outPut.next=list1 if list1 else list2

        return result.next