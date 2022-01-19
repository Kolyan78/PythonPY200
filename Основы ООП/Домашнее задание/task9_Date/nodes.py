from typing import Any, Optional
class LinkedList:
    def __init__(self, data):
        self.list_nodes: list[Node] = []
        self.head: Node = None
        self.len: int = 0

        self.init_linked_list(data)

    def __repr__(self):
        return f"{self.list_nodes}"

    def init_linked_list(self, data):
        self.list_nodes = [Node(value) for value in data]
        self.head = self.list_nodes[0]
        self.len = len(self.list_nodes)

        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]  # берём текущий узел
            next_node = self.list_nodes[i + 1]  # берём следующий узел

            self.linked_nodes(current_node, next_node)  # связываем их

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional["Node"] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)


list_ = [1, 2, 3]
linked_list = LinkedList(list_)
print(linked_list)