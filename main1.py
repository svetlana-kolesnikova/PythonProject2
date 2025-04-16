from typing import Iterable


def same_num(list_1: Iterable[int], list_2: Iterable[int]) -> Iterable[int]:
    """функция выводит список из элементов встречающихся в обоих входных списках"""
    list_new = list_1 + list_2
    dubl_num = set()
    for num in list_new:
        if list_new.count(num) > 1:
            dubl_num.add(num)

    return list(dubl_num)


# Пример вывода:
# [3, 4]

print(same_num([1, 2, 3, 4], [3, 4, 5, 6]))


students_data = {"Анна": 4.5, "Иван": 3.8, "Мария": 4.2, "Петр": 3.5}
# Запросите пользователя ввести имя студента, которого нужно удалить. Удалите # # студента из словаря, и выведите обновленный словарь.

delite_name = input("Enter name: ")
del students_data[delite_name]

print(students_data)

