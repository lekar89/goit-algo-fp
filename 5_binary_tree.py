import networkx as nx
import matplotlib.pyplot as plt


class HeapNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.id = id(self)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.key)  # Додано label для вузлів купи
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_colors(num_steps):
    # Початковий темний колір (темно-синій)
    base_color = (18, 150, 240)
    # Генеруємо список кольорів
    colors = []
    for step in range(num_steps):
        # Додаємо до базового кольору значення для кожного каналу
        step_color = tuple(
            int(base_channel + (255 - base_channel) * step / num_steps)
            for base_channel in base_color
        )
        # Додаємо кольор у список
        colors.append("#%02x%02x%02x" % step_color)
    return colors


def draw_heap(heap_root, traversal):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    # Генеруємо кольори для кожного кроку обходу
    num_steps = len(traversal)
    colors = generate_colors(num_steps)

    plt.figure(figsize=(8, 5))
    # Використовуємо цикл для присвоєння кольорів вузлам у графі
    for step, (node_id, _) in enumerate(traversal):
        heap.nodes[node_id]["color"] = colors[step]

    nx.draw(
        heap,
        pos=pos,
        labels=nx.get_node_attributes(heap, "label"),  # Використовуємо мітки для вузлів
        node_color=[heap.nodes[node]["color"] for node in heap.nodes()],
        with_labels=True,
        arrows=False,
        node_size=2500,
    )
    plt.show()


# Виконуємо обхід бінарного дерева у глибину (інфіксний обхід).
def inorder_traversal(node, traversal):
    if node:
        inorder_traversal(node.left, traversal)
        traversal.append((node.id, node.key))
        inorder_traversal(node.right, traversal)


# Виконуємо обхід бінарного дерева у ширину.
def breadth_first_traversal(root, traversal):
    queue = [root]
    while queue:
        node = queue.pop(0)
        traversal.append((node.id, node.key))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


heap_root = HeapNode(1)
heap_root.left = HeapNode(2)
heap_root.right = HeapNode(3)
heap_root.left.left = HeapNode(4)
heap_root.left.right = HeapNode(5)

# Обходи дерева
inorder = []
inorder_traversal(heap_root, inorder)

breadth_first = []
breadth_first_traversal(heap_root, breadth_first)

# Візуалізація обходів
print("Обхід бінарного дерева у глибину:")
print(inorder)
draw_heap(heap_root, inorder)

print("Обхід бінарного дерева у ширину:")
print(breadth_first)
draw_heap(heap_root, breadth_first)
