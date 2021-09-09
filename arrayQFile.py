from array import array


class ArrayQ:
    def __init__(self):
        self.__array = array("i")

    def enqueue(self, data):
        self.__array.insert(0, data)

    def dequeue(self):
        return self.__array.pop(-1)

    def isEmpty(self):
        if len(self.__array) == 0:
            return True
        else:
            return False
