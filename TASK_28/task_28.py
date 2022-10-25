# Task 1
# Extend UnorderedList
# Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two parameters `start` and `stop`, and return a copy of the list starting at the position and going up to but not including the stop position.

# Task 2
# Implement a stack using a singly linked list.


# Task 3
# Implement a queue using a singly linked list.


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):  # отримує
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):  # перезаписує
        self._data = data

    def set_next(self, new_next):  # встановлує наступне
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        if not self.search(item):
            return
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # Task 1
    def info(self):
        l_list = []
        current = self._head
        while current is not None:
            l_list.append(current.get_data())
            current = current.get_next()
        return l_list

    # if you can implement it as a magic method - that would be awesome
    def __getitem__(self, subscript):
        result = self.info().__getitem__(subscript)
        if isinstance(subscript, slice):
            return list(result)
        else:
            return result

    def get_slice(self, start, stop):
        return self.info()[start:stop]

    def append(self, item):
        return self.info().append(item)

    def index(self, item):
        return self.info().index(item)

    def pop(self, index):
        return self.info().pop(index)

    def insert(self, index, item):
        return self.info().insert(index, item)

    # Task 2
    def peek(self):  # Повернутись до верхнього елемента стека
        if not self.info():
            return None
        return self.info()[-1]

    # Task 3
    def dequeue(self, item):  # Додати елемент на початок черги
        self.info().insert(0, item)

    def enqueue(self):  # Видалити елемент із заголовка черги
        return self.info().pop()

    def __repr__(self):  # Перероблено з нижче вказаного
        # current = self._head
        # while current is not None:
        #     representation += f"{current.get_data()} "
        #     current = current.get_next()
        # return representation + ">"
        # pass

        representation = "<UnorderedList: "
        for i in self.info():
            representation += f'{i} '
        return representation + '>'


if __name__ == "__main__":
    my_list = UnorderedList()
    # simple option:
    # my_list.get_slice(start, stop)

    # advanced option:
    # my_list[start:stop]

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(32)
    print(my_list.size())
    print(my_list.search(93))

    print(my_list.info())
    print(my_list.get_slice(1, 3))
    print(my_list[1:3])  # using magic method
