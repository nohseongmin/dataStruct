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
        curr = self.head # 처음껄 지우면 링크가 지워지지 않음
        if self.head.data == target:
            self.head = self.head.link
            curr.link = None
            return
        prev = None
        while curr:
            if target == curr.data:
                prev.link = curr.link
                #지울 노드와 그 다음 노드가 연결됨. 그걸 끊어 GC가 알아서 지우게 함
                curr.link = None
            prev = curr
            curr = curr.link

    def search(self, target):
        current = self.head
        while current: #.link를 넣으면 마지막줄을 검증못함 bug.fix
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
ll.append(10)
ll.append(15)
print(ll)
print(ll.search(99))
print(ll.search(10))
ll.remove(10)
print(ll)