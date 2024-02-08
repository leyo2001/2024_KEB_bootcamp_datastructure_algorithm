class Node:
    def __init__ (self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def insertNode(findData, insertData):
    global head, current, pre

    node = Node()
    node.data = insertData

    if head.data == findData :      # 첫 번째 노드 삽입

        node.link = head
        head = node
        return

    current = head
    while current.link != None :    # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData :
            node.link = current
            pre.link = node
            return

    current.link = node             # 마지막 노드 삽입






head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__" :

    node = Node()		# 첫 번째 노드
    node.data = dataArray[0]
    head = node


    for data in dataArray[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node


    printNodes(head)
    insertNode("쯔위", "윤석")
    printNodes(head)
