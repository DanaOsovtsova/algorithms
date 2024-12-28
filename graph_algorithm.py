with open("in.txt", "r") as f:
    keys = [int(line.strip()) for line in f if line.strip()]

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# добавление нового узла в дерево
def insert(root, key):
    if root is None:
        return TreeNode(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# высота
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

# количество потомков узла
def count_children(node):
    if not node:
        return 0
    return 1 + count_children(node.left) + count_children(node.right)

# узлы на уровне h/2
def find_nodes_at_level(node, level, current_level, nodes):
    if not node:
        return
    if current_level == level:
        nodes.append(node)
    find_nodes_at_level(node.left, level, current_level + 1, nodes)
    find_nodes_at_level(node.right, level, current_level + 1, nodes)

# правое удаление
def remove_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = remove_node(root.left, key)
    elif key > root.val:
        root.right = remove_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # находим минимальный в правом, меняем и удаляем
        min_larger_node = root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        root.val = min_larger_node.val
        root.right = remove_node(root.right, min_larger_node.val)
    return root

# прямой левый обход дерева корень-левое-правое
def pre_order_traversal(node, result):
    if node:
        result.append(node.val)
        pre_order_traversal(node.left, result)
        pre_order_traversal(node.right, result)

# дерево
root = None
for key in keys:
    root = insert(root, key)

# высота дерева
H = height(root)
level_to_check = H // 2

# узлы на уровне h/2
nodes_at_level = []
find_nodes_at_level(root, level_to_check, 0, nodes_at_level)

# фильтруем узлы: у которых количество потомков в левом поддереве больше, чем в правом
filtered_nodes = [node for node in nodes_at_level if count_children(node.left) > count_children(node.right)]

# Удаляем узел только если количество узлов нечетное
if filtered_nodes and len(filtered_nodes) % 2 != 0:
    filtered_nodes.sort(key=lambda x: x.val)
    middle_index = len(filtered_nodes) // 2
    node_to_remove = filtered_nodes[middle_index].val

    # удаляем узел
    root = remove_node(root, node_to_remove)

# прямой левый обход
result = []
pre_order_traversal(root, result)

# запись результата в файл
with open("out.txt", "w") as f:
    for val in result:
        f.write(f"{val}\n")
