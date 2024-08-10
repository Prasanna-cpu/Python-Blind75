class ListNode:
    def __init__(self,val=0,next=None):
        self.next = next
        self.val=val



def mergeLists(list1,list2):
    dummy=ListNode()
    curr=dummy


    while list1 and list2:
        if list1.val<=list2.val:
            curr.next=list1
            list1=list1.next
        else:
            curr.next=list2
            list2=list2.next

        curr=curr.next

    if list1:
        curr.next = list1
        list1 = list1.next
    if list2:
        curr.next = list2
        list2 = list2.next

    return dummy.next

def printList(head: ListNode):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    # Creating first linked list: 1 -> 3 -> 5 -> None
    list1 = ListNode(1, ListNode(3, ListNode(5)))

    # Creating second linked list: 2 -> 4 -> 6 -> None
    list2 = ListNode(2, ListNode(4, ListNode(6)))

    print("List 1:")
    printList(list1)

    print("List 2:")
    printList(list2)

    # Merging the two lists

    merged_list = mergeLists(list1, list2)

    print("Merged List:")
    printList(merged_list)
