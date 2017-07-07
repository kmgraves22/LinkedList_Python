# @author: Kevin Graves
# runs tests for LinkedList.py
from LinkedList import *

def main():
   list = LinkedList()
   print("Insert Test: expected out 3, 2, 1")
   list.insert(1)
   list.insert(2)
   list.insert(3)
   list.printList()
   print("Remove Test: expected out 3, 1")
   list.delete(2)
   list.printList()
   print("Remove Duplicates: expected out 3, 2, 1")
   list2 = LinkedList()
   list2.insert(1)
   list2.insert(2)
   list2.insert(3)
   list2.insert(1)
   list2.insert(2)
   list2.insert(3)
   list2.insert(1)
   list2.insert(2)
   list2.insert(3)
   list2.removeDups()
   list2.printList()

if __name__ == '__main__':
   main()