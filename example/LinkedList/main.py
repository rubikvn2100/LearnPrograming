from SortedLinkedList import SortedLinkedList

if __name__ == "__main__":
    sll = SortedLinkedList()

    print()
    
    sll.insert(3)
    sll.insert(5)
    sll.insert(2)
    sll.show()
    
    print()

    for i in range(1, 7):
        print(f"Try to find val {i} and the result is {sll.find(i)}")

    print()

    print(f"Test if the linked list is empty or not: {sll.isEmpty()}")

    print()

    sll.remove(3)
    sll.show()

    sll.remove(5)
    sll.show()

    sll.remove(2)
    sll.show()

    print()

    print(f"Test if the linked list is empty or not: {sll.isEmpty()}")

    print()