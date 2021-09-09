from linkedQFile import LinkedQ


def trollkarlstricket(data):
    queue = LinkedQ()
    listan = data.split(" ")

    for i in listan:
        queue.enqueue(i)

    while not queue.isEmpty():
        queue.enqueue(queue.dequeue())
        print(queue.dequeue(), end=" ")


trollkarlstricket(input())
