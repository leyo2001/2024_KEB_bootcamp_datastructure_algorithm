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

def plus_minus():
    plus_cnt , minus_cnt = 0, 0
    current = head
    while True:
        if current.data > 0:
            plus_cnt += 1
            current.data *= -1
        elif current.data <0:
            minus_cnt += 1
            current.data *= -1
        else:
            pass
        if current.link == head:
            break
        current = current.link

    print(f"양수--> {plus_cnt}\t 음수--> {minus_cnt}")





if __name__ == "__main__":
    array = []
    for i in range(0,7):
        array.append(random.randint(-100,201))

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
    plus_minus()
    print_node()






