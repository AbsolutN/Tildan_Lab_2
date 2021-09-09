from array import array


class ArrayQ:
    def __init__(self):
        # Skapar ett array object
        self.__array = array("i")

    def enqueue(self, data):
        # Lägger till objekt i början av listan
        self.__array.insert(0, data)

    def dequeue(self):
        # Lägger till objekt i början av listan
        return self.__array.pop(-1)

    def isEmpty(self):
        # kollar om kön är tom
        if len(self.__array) == 0:
            # Returnerar True om den är tom
            return True
        else:
            # Returnerar False om den inte är tom
            return False
