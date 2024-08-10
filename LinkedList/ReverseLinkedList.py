

class ListNode:
    def __init__(self,val=0,next=None):
        self.next = next
        self.val=val




def reverseList(head):
    if head is None or head.next is None:
        return head

    new_head=reverseList(head.next)
    head.next.next=head
    head.next=None

    return new_head

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    # Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original list:")
    printList(node1)

    # Reversing the linked list
    reversed_head = reverseList(node1)

    print("Reversed list:")
    printList(reversed_head)

