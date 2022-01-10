from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise ...  # TODO подставьте нужную ошибку

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        # TODO

    def to_list(self) -> list:
        ...  # TODO Метод to_list реализовать через list comprehension.

    def __repr__(self) -> str:
        ...  # TODO c помощью метода to_list реализовать данный метод

    def __str__(self) -> str:
        ...  # TODO c помощью метода to_list реализовать данный метод


if __name__ == '__main__':
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)

    print(linked_list)
    print(repr(linked_list))
