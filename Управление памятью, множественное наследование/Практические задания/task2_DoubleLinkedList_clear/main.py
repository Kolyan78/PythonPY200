from typing import Any, Optional
import weakref

from node import Node
from linked_list import LinkedList


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None, next_: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev  # TODO объект теперь вызываемый

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev  # TODO сделать слабую ссылку

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"  # todo make all

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"


class DoubleLinkedList(LinkedList):
    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    ll = DoubleLinkedList([1, 2, 3, 4, 5])

    ll.clear()

    print(ll)
