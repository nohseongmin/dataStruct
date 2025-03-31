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
            #result = result + str(current.data) + "->"
            result = result + f"{current.data} -> "
            current = current.link
        return result


#리스트생성 -> init메소드 동작 -> 링크드리스트 객체 생성, head 속성(none값) 들어감
ll = LinkedList()
#data값에 8이 전달, head가 none이므로 if문 동작, self.head에 새로 생긴 노드(8)의 주소값 넣음, 이후 리턴
ll.append(8)
#if문 동작 X, current (지역변수)에 self.head의 주소값 대입, current.link는 none이므로 while문 생략,
#current.link에 Node(10) 넣음. 10의 주소값
ll.append(10)
ll.append(9)
print(ll)
print(ll.search(10))
print(ll.search(11))
