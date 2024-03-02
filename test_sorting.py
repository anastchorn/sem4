from sorting import sort_list
import pytest

def test_sort_list():
    assert sort_list([3, 2, 1]) == [1, 2, 3], "Список не відсортовано правильно"
    assert sort_list([5, -1, 0]) == [-1, 0, 5], "Неправильне сортування з від'ємними числами"
    assert sort_list([]) == [], "Помилка сортування пустого списку"
    assert sort_list([1]) == [1], "Список з одного елемента змінений"
    assert sort_list([1, 1, 1]) == [1, 1, 1], "Неправильне сортування списку з однаковими елементами"
