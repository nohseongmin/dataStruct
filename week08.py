def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end="->")

def pre_order(node):
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        cur = root
        while True:
            #현재노드가 저장된값보다 큰가?
            if number < cur.data:
                #작으면 왼쪽에 넣기
                if cur.left is None:
                    cur.left = node
                    break
                #만약 none이 아니면 이동
                cur=cur.left
            else:
                #크면 오른쪽
                if cur.right is None:
                    cur.right = node
                    break
                cur=cur.rigth
    print("bst 구성완료")
    #중위순회 해야 순서대로(큰순서대로) 나옴
    in_order(root)



