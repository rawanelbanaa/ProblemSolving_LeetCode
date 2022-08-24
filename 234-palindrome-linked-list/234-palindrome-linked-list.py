# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        curnt = head
        
        while curnt:
            temp.append(curnt.val)
            curnt = curnt.next

        if temp == temp[::-1]:
            return True
        return False