# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        while len(lists) > 1: 
            new_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                new_list.append(self.mergeTwoLists(l1, l2))

            lists = new_list
        
        return(lists[0])


    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next,list1
            else: 
                cur.next = list2
                list2, cur = list2.next, list2
        
        cur.next = list1 or list2
        
        return dummy.next

        
