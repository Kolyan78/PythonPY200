from typing import Any, Optional

class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_node: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_node: следующий узел, если он есть
        """
        self.value = value
        self.next_node = next_node
    def __repr__(self):
        return f"Node({self.value}, {self.next_node})"

if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)
    first_node.next_node = second_node
    print(first_node)
    print(second_node)