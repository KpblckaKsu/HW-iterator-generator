# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и
# возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = iter(list_of_list)

    def __iter__(self):
        self.flat_list = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.flat_list)
        except StopIteration:
            self.flat_list = iter(next(self.list_of_list))
            item = next(self.flat_list)

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

# Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и
# возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.

import types

def flat_generator(list_of_lists):
    flat_list = []
    for list_one in list_of_lists:
        flat_list.extend(list_one)
    for item in flat_list:
        yield item

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
