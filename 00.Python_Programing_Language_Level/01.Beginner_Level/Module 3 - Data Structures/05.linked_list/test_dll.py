from doubly_linked_list import * 

def test_append():
    dll = Doubly_linked_list()
    assert dll.head.next == None,"linked list empty,so head should point to none"
    item = 5
    dll.append(item)
    assert dll.head.next.data == item,"head should point to the first node"
     