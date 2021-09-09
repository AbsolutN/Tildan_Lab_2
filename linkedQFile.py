class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:

    def __init__(self):
        self.__first = None
        self.__last = None

    def isEmpty(self):
        if self.__first is None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)
        if self.__first is None:
            self.__first = new_node
            self.__last = self.__first
        else:
            self.__last.next = new_node
            self.__last = new_node

    def dequeue(self):
        if self.__first is not None:
            x = self.__first.value
            self.__first = self.__first.next
            return x
