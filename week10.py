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

def search(find_number):
    current = root
    while True:
        if find_number == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
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

def delete(node, value):
    if node is None:
        return None
    if value < node.data:
        node.left = delete(node.left, value)
        return node
    elif value > node.data:
        node.right = delete(node.right, value)
        return node
    else:
        #leaf 노드 / 자식이 1개인경우 노드 삭제
        if node.right is None:
            return node.right
        elif node.left is None:
            return node.left
        # min_larger_node = node.right
        # #curr 의 left가 none 일 때까지 이동
        # while  min_larger_node.left:
        #     min_larger_node = min_larger_node.left
        #     #이동 후 대입
        # node.data = min_larger_node.data
        # #이동 후 삭제
        # node.right = delete(node.right, min_larger_node.data)
        max_smaller_node = node.left
        while max_smaller_node.right:
            max_smaller_node = max_smaller_node.right
        node.data = max_smaller_node.data
        node.right = delete(node.left, max_smaller_node.data)
    return node

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 100, 7, 13]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("bst 구성완료")
    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()
    find_number = int(input("찾는 수:"))
    if search(find_number):
        print(f"{find_number}를 찾았습니다.")
    else:
        print(f"{find_number}는 존재하지 않습니다.")

    delete_number = int(input("삭제할 수 :"))
    root = delete(root, delete_number)

    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()
