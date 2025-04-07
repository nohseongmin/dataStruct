class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            #raise IndexError("스택 비어있음")
            return "stack is empty!"
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None
        return popped_node.data


s1 = Stack()
print(s1.pop()) #빈 스택이라 예외처리됨
s1.push("data Struct")
s1.push("dataBase")
print(s1.pop())
print(s1.pop())