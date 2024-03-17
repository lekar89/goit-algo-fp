import networkx as nx
import matplotlib.pyplot as plt


# Клас, що представляє вузол бінарної купи
class HeapNode:
    def __init__(self, key, left=None, right=None):
        self.key = key  # Ключ вузла
        self.left = left  # Посилання на лівого сина
        self.right = right  # Посилання на правого сина
        self.id = id(self)  # Унікальний ідентифікатор вузла


# Функція для додавання вузлів та ребер бінарної купи до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додавання вузла до графа з використанням id та мітки (значення ключа вузла)
        graph.add_node(node.id, label=node.key)
        # Додавання ребра та лівого сина до графа
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        # Додавання ребра та правого сина до графа
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


# Функція для візуалізації бінарної купи
def draw_heap(heap_root):
    # Створення спрямованого графа
    heap = nx.DiGraph()
    # Початкове розташування кореня купи
    pos = {heap_root.id: (0, 0)}
    # Додавання вузлів та ребер до графа
    heap = add_edges(heap, heap_root, pos)

    # Задання розміру графіка
    plt.figure(figsize=(8, 5))
    # Відображення графа з використанням міток вузлів та без стрілок
    nx.draw(
        heap,
        pos=pos,
        labels=nx.get_node_attributes(heap, "label"),  # Використання міток для вузлів
        with_labels=True,  # Відображення міток вузлів
        arrows=False,
        node_size=2500,
        node_color="skyblue",  # Задання кольору вузлів
    )
    plt.show()


# Створення кореня купи та додавання вузлів
heap_root = HeapNode(1)
heap_root.left = HeapNode(2)
heap_root.right = HeapNode(3)
heap_root.left.left = HeapNode(4)
heap_root.left.right = HeapNode(5)

# Відображення бінарної купи
draw_heap(heap_root)
