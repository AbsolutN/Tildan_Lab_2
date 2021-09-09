
import unittest
from array import array
from arrayQFile import ArrayQ
from linkedQFile import LinkedQ


# Uppgift1
def experiment():
    my_array = array('i')

    my_array.append(12)
    my_array.append(13)
    print(my_array)

    my_array.insert(0, 112)
    my_array.append(12)
    my_array.append(12)
    my_array.append(12)
    my_array.append(100)
    print(my_array)

    my_array.remove(12)
    print(my_array)

    my_array.pop(-1)
    print(my_array)

# experiment()


def arrayQTest():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if x == 1 and y == 2:
        print("OK")
    else:
        print("FAILED")

# arrayQTest()


def trollkarlstricket(data):
    queue = ArrayQ()
    listan = data.split(",")

    # Lägger till alla värden i kön
    for i in listan:
        queue.enqueue(int(i))

    while not queue.isEmpty():
        # Tar ut nästa i kön och lägger det sist
        queue.enqueue(queue.dequeue())
        # Lägger ut nästa i kön på bordet (printar ut värdet)
        print(queue.dequeue())


if __name__ == '__main__':
    trollkarlstricket("7,1,12,2,8,3,11,4,9,5,13,6,10")


class TestQueue(unittest.TestCase):

    def test_isEmpty(self):
        # isEmpty ska returnera True för tom kö, False annars
        q = LinkedQ()
        self.assertTrue(q.isEmpty(), "isEmpty på tom kö")
        q.enqueue(17)
        self.assertFalse(q.isEmpty(), "isEmpty på icke-tom kö")

    def test_order(self):
        # Kontrollerar att kö-ordningen blir rätt
        q = LinkedQ()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)


if __name__ == "__main__":
    unittest.main()
