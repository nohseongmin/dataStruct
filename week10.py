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

def search():
    find_number = int(input("찾는 수:"))
    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다")
            break
        elif find_number < current.data:
            if current.left is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.right
def insert(root, value):
    node = TreeNode()
    node.data = value
    if root is None:
        return node

    cur = root
    while True:
        # 현재노드가 저장된값보다 큰가?
        if value < cur.data:
            # 작으면 왼쪽에 넣기
            if cur.left is None:
                cur.left = node
                break
            # 만약 none이 아니면 이동
            cur = cur.left
        else:
            # 크면 오른쪽
            if cur.right is None:
                cur.right = node
                break
            cur = cur.right
    #지역변수 root 값을 return 해야 밖에서도 사용가능
    return root

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("bst 구성완료")
    #중위순회 해야 순서대로(큰순서대로) 나옴
    in_order(root)
    print()
    search()
