class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:

    def __init__(self):
        self.__first = None
        self.__last = None


    def enqueue(self, data):
        """
        Lägger till parametern data sist i kön
        :param data: värdet som ska läggas till i listan
        :return: inget
        """
        newNode = Node(data)
        if self.__first == None:
            self.__first = newNode
        else:
            ...


    def dequeue(self):
        """

        :return: det första värdet i kön
        """


    def isEmpty(self):
        """
        Kollar om listan är tom eller inte
        :return: True om listan är tom, False om listan innehåller något
        """
        if self.__first == None:
            return True
        else:
            return False


q = LinkedQ()
print(q.isEmpty())