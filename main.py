
# AUFGABE 1 bis 3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size


    def clear(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
        return


    def get_data(self, data):
        current = self.head
        while current:
            value = current.data.data
            current = current.next
            if value == data.data:
                return value

    def delete(self, data):
        if self.head.data.data == data.data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            current = self.head
            currentNext = self.head.next

            while currentNext != None:

                prev = current
                current = current.next
                currentNext = currentNext.next

                if current.data.data == data.data:
                    if currentNext == None:
                        prev.next = None
                        List.size -= 1
                        return
                    else:
                        prev.next = prev.next.next
                        List.size -= 1
                        return

            return



List = SinglyLinkedList()


#Überprüfung Aufgabe 1
node1 = Node(1)
node2 = Node(2)
List.append(node1)
List.append(node2)

print(List.get_size())
List.clear()
print(List.get_size())


# Überprüfung Aufgabe 2
node3 = Node('er')
List.append(node1)
List.append(node2)
List.append(node3)

print(List.get_data(node3))
print(List.get_size())


#Überprüfung Aufgabe 3
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
List.append(node4)
List.append(node5)
List.append(node6)

print(List.get_size())
print(List.get_data(node2))
List.delete(node2)
print(List.get_size())



# AUFGABE 5

class MyStack:

    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)
        return element

    def pop(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop()


    def top(self):
        if self.items == []:
            return 0
        else:
            return self.items[-1]


    def size(self):
        return len(self.items)


#Überprüfung Aufgabe 5
stack = MyStack()

stack.push('quick')
stack.push('brown')
stack.push('fox')

print(stack.top())
print(stack.pop())
print(stack.top())
print(stack.size())




# AUFGABE 6

class MyQueue:

    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)
        return element

    def pop(self):
        if self.items == []:
            return 0
        else:
            return self.items.pop(0)

    def show_left(self):
        try:
            return self.items[-1]
        except:
            print('Error')
            return

    def show_right(self):
        try:
            return self.items[0]
        except:
            print('Error')
            return

    def size(self):
        return len(self.items)


#Überprüfung Aufgabe 6
queue = MyQueue()

queue.push('quick')
queue.push('brown')
queue.push('fox')

print(queue.show_left())
print(queue.show_right())
print(queue.pop())

