class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Приклад використання:

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("До реверсування:")
linked_list.print_list()

linked_list.reverse()

print("Після реверсування:")
linked_list.print_list()


def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    sorted_head = None
    current = head

    while current:
        next_node = current.next
        sorted_head = insert_sorted(sorted_head, current)
        current = next_node

    return sorted_head


def insert_sorted(sorted_head, new_node):
    if not sorted_head or new_node.data <= sorted_head.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return sorted_head


# Приклад використання:

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(4)
linked_list.append(2)
linked_list.append(5)

print("\nДо сортування:")
linked_list.print_list()

sorted_head = insertion_sort_linked_list(linked_list.head)

sorted_linked_list = LinkedList()
sorted_linked_list.head = sorted_head

print("Після сортування вставками:")
sorted_linked_list.print_list()


def merge_sorted_linked_lists(head1, head2):
    dummy_node = Node(0)
    current = dummy_node

    while head1 and head2:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    return dummy_node.next


# Приклад використання:

linked_list1 = LinkedList()
linked_list1.append(1)
linked_list1.append(3)
linked_list1.append(5)

linked_list2 = LinkedList()
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(6)

print("\nПерший відсортований список:")
linked_list1.print_list()

print("Другий відсортований список:")
linked_list2.print_list()

merged_head = merge_sorted_linked_lists(linked_list1.head, linked_list2.head)

merged_linked_list = LinkedList()
merged_linked_list.head = merged_head

print("Після об'єднання відсортованих списків:")
merged_linked_list.print_list()
