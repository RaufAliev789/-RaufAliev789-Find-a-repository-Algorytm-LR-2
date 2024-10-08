class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def height(root): #Вычисление высоты дерева
    return 0 if not root else 1 + max(height(root.left), height(root.right))

def insert(root, val): #Вставка узла
    if root is None:
        return Node(val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Ввод данных
n = int(input("Введите количество узлов: "))
values = list(map(int, input("Введите значения узлов через пробел: ").split()))

# Построение бинарное дерево
root = None
for value in values:
    root = insert(root, value)

# Вывод высоты дерева
print("Высота бинарного дерева:", height(root)-1)