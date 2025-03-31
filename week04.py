class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    #내가만든 링크드 리스트에 값을 넣을 함수
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        #현재 노드의 링크
        while current.link:
            current = current.link
        current.link = Node(data)

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.link
            return
        curr = self.head
        prev = None
        while curr:
            if target == curr.data:
                prev.link = curr.link
            prev = curr
            curr = curr.link

    def search(self, target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}은(는) 존재하지 않습니다."

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} -> "
            current = current.link
        return result + "END"

ll = LinkedList()
ll.append(99)
ll.append(12)
ll.append(15)
print(ll)
print(ll.search(99))
print(ll.search(10))
ll.remove(12)
print(ll)