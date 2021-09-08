from array import array

# Uppgift1
def experiment():
    my_array = array('i')

    my_array.append(12)
    my_array.append(13)

    print(my_array)

    my_array.insert(0,112)
    my_array.append(12)
    my_array.append(12)
    my_array.append(12)
    my_array.append(100)

    print(my_array)

    my_array.remove(12)

    print(my_array)

    my_array.pop(-1)

    print(my_array)

#experiment()


# Uppgift 2
def arrayQTest():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")

#arrayQTest()


# Uppgift 3
def trollkarlstricket(data):
    queue = ArrayQ()
    listan = data.split(",")

    # Lägger till alla värden i listan
    for i in listan:
        queue.enqueue(int(i))

    while queue.isEmpty():
        # Tar ut nästa i kön och lägger det sist
        queue.enqueue(queue.dequeue())
        # Lägger ut nästa i kön på bordet (printar ut värdet)
        print(queue.dequeue())



