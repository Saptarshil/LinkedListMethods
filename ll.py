class Node:  #This class creates a node object which will contain the value and the next pointer pointing to the next node.
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList: #This class creates the linklist.
    def __init__(self, value):
        new_node = Node(value) #This creates a node object and assigns its length and the header and tail pointer.
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def appendll(self, value): #add an element at the last
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def popll(self): #remove the last element
        if self.length == 0: #we have 3 different conditons: its alreday empty, has only 1 node and has multiple nodes.
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            while temp.next.next is not None: #we find out the penultimate node and dettach the last node from it while pointing the tail at this node
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1
            return temp

    def prependll(self, value): #adding at the very start of the ll
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def popfirstll(self): #removing the first node
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp

    def getll(self, index): #returns the node present in the given index
        if self.length <= index < 0:
            return None
        else:
            temp = self.head
            for _ in range(index): #_ is used in place of a variable because we wont be using the variable inside the loop.
                temp = temp.next
            return temp

    def setll(self, index, value): #change the value of node at the desired index
        temp = self.getll(index)
        if temp is None:
            return False
        else:
            temp.value = value
            return True

    def insertll(self, index, value):#insert a new node at the desired index
        new_node = Node(value)
        if self.length <= index < 0:
            return False
        elif index == 0: #we have alreday defined fucntions to add nodes at both ends of the ll.
            return self.prependll(value)
        elif index == self.length-1:
            return self.appendll(value)
        else:
            temp = self.getll(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def removell(self, index): #remove a node at the desired index
        if self.length <= index < 0:
            return False
        elif index == 0:
            return self.popfirstll()
        elif index == self.length-1:
            return self.popll()
        else:
            prev = self.getll(index-1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return True

    def reversell(self): #reverse the order of the nodes
        if self.length == 0:
            return False
        elif self.length ==1:
            return True
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp #the pointers here point in reverse. This is the step that enables them to do so.
                temp = after
            return True

    def printll(self):
        temp = self.head
        while temp is not None: #On the last node temp.next will point to none. then temp=temp.next which means that temp will become none.
            print("Node is : "+str(temp.value))
            temp = temp.next


new_ll = LinkedList(10)
new_ll.appendll(24)
new_ll.appendll(69)
new_ll.prependll(0)
new_ll.printll()
new_ll.reversell()
new_ll.printll()
