# @author: Kevin Graves
# Progam: Implementation of a linked list in python 3

class Node(object):
   
   def __init__(self, data = None, next_node = None):
      self.data = data
      self.next_node = next_node
      
   def get_data(self):
      return self.data
      
   def get_next(self):
      return self.next_node
      
   def set_next(self, temp_next):
      self.next_Node = temp_next
      
class LinkedList(object):
   def __init__(self, head = None):
      self.head = head
      
   # inserts a node to the start of list
   def insert(self, data):
      new = Node(data)
      new.next_node = self.head
      self.head = new
      
   def size(self):
      curr = self.head
      count = 0
      while curr:
         count += 1
         curr = curr.next_node
      return count
   
   # searches for node with data, returns the node or None if node not found
   def search(self, data):
      curr = self.head
      while curr:
         if curr.data == data:
            return curr
         curr = curr.next_node
      return None
   
   # finds node with given data and deletes it from the list, does nothing if data not found
   def delete(self, data):
      curr = self.head
      prev = None
      while curr:
         if curr.data == data:
            prev.next_node = curr.next_node
            return
         prev = curr
         curr = curr.next_node
   
   ##start of more interesting functions
   
   #removes duplicate nodes from list
   def removeDups(self):
      D = {}
      curr = self.head
      prev = None
      while curr:
         if D.get(curr.data) == 1:
            prev.next_node = curr.next_node
            curr = prev
         else:
            D[curr.data] = 1
         prev = curr
         curr = curr.next_node
      
   def printList(self):
      curr = self.head
      while curr:
         print(curr.data)
         curr = curr.next_node
      
   #  this functions returns the kth to last element
   #  if the kth to last element does not exist returns None
   def returnKthtoLast(self, k):
      size = self.size()
      if k >= size:
         return None
      curr = self.head
      index = size - k - 1
      while index > 0:
         curr = curr.next_node
         index -= 1
      return curr.data
         
      
      
     