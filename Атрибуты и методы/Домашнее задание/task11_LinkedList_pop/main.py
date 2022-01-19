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

    def index(self, value: Any, start=0, end=None):
        """Возвращает индекс указанного элемента
        :param value: значение элемента
        :return: индекс первого найденнго элемента
        Тут я хотел добавить возможность указывать начальный и конечный индексы
        для указания диапазона поиска, но пока еще не получилолсь реализовать это((
        """
        # if end == None:
        #     end = self.len - 1
        # if end > self.len:
        #     raise IndexError ("Слишком большой индекс")
        current_node = self.head
        for i in range(self.len):
            if i < start:
                break
            if current_node.value == value:
                 return i
            current_node = current_node.next
        raise ValueError (f"{value} в этом списке отсутствует")

    def count(self, value: Any):
        """Возвращает количество вхождений указанного элемента
        :param value: значение элемента
        :return: количество вхождений
        Использовал предыдущий метод, с небольшими изменениями: при нахождении элемента счетчик
        увеличивается, и так продолжается до тех пор пока список не закончится.
        """
        j = 0
        current_node = self.head
        for i in range(self.len):
            if current_node.value == value:
                j += 1
            current_node = current_node.next
        if j == 0:
            raise ValueError(f"{value} в этом списке отсутствует")
        return j

    def extend(self, list2: Iterable):
        """Склеивает два списка
        :param list2: второй список, который надо приклеить к первому
        :return: ничего не возвращает
        Здесь используется уже реализованный ранее метод append
        """
        for value in list2:
            self.append(value)

    def pop(self, index=None):
        """Удаляет элемент по указанному индексу
        или если аргумент не указан, удаляет последний элемент списка
        Я здесь использовал ранее реализованный метод __delitem__
        А можно ли сделать так, чтобы не искользовать одинаковый код дважды, а прямо здесь
        вызвать метод del? Но как ему указать на экземпляр объекта?"""
        if index == None:
            index = self.len - 1
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:  # для for
            raise IndexError()
        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next
            self.linked_nodes(prev_node, next_node)
        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self.len += 1


if __name__ == '__main__':
    list_ = [1, 2, 3, 2, 5, 2, 7, 8]
    list2_ = [9, 10, 11, 12, 13, 14, 15, 16]
    linked_list = LinkedList(list_)
    print(linked_list)

    linked_list.insert(0, 0)
    linked_list.insert(len(linked_list), len(linked_list))
    linked_list.insert(100, 100)
    linked_list.insert(2, "wow")
    print(linked_list)

    """Реализация метода index"""
    print(linked_list.index(3))
    """Реализация метода count"""
    print(linked_list.count(2))
    """Склеим существующий список и список list2_"""
    linked_list.extend(list2_)
    print(linked_list)
    """Удалим последний элемент (16) и напечатаем получившийся список"""
    linked_list.pop()
    print(linked_list)
    """Удалим нулевой элемент (0) и напечатаем получившийся список"""
    linked_list.pop(0)
    print(linked_list)
    """Удалим первый элемент ('wow') и напечатаем получившийся список"""
    linked_list.pop(1)
    print(linked_list)
    """Удалим двенадцатый элемент (11) и напечатаем получившийся список"""
    linked_list.pop(12)
    print(linked_list)