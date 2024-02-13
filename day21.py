import random

class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_node():
    current = head
    while True:
        print(current.data, end = " ")
        if current.link == head:
            break
        current = current.link
    print()

def odd_even():
    odd_cnt , even_cnt = 0, 0
    current = head
    while True:
        if current.data % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
        if current.link == head:
            break
        current = current.link


    if even_cnt > odd_cnt:
        current = head
        while True:
            if current.data % 2 == 0:
                current.data *= -1
            else:
                pass
            if current.link == head:
                break
            current = current.link


    else:
        current = head
        while True:
            if current.data % 2 == 0:
                pass
            else:
                current.data *= -1
            if current.link == head:
                break
            current = current.link



if __name__ == "__main__":
    array = []
    for i in range(0,7):
        array.append(random.randint(1,100))

    node = Node()
    node.data = array[0]
    head = node
    node.link = head

    for number in array[1:]:
        pre = node
        node = Node()
        node.data = number
        pre.link = node
        node.link = head

    print_node()
    odd_even()
    print_node()






