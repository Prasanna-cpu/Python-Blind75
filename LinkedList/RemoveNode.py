

class ListNode:
    def __init__(self,val=0,next=None):
        self.next = next
        self.val=val


def removeNode(head,n):
    start=ListNode()
    start.next=head

    fast=slow=start

    for _ in range(n+1):
        fast=fast.next

    while fast:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return start.next

def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    # Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original list:")
    printList(head)

    # Remove the 2nd node from the end (which is the node with value 4)
    n = 2
    modified_head = removeNode(head, n)

    print(f"List after removing {n}th node from the end:")
    printList(modified_head)