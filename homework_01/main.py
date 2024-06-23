"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 
            for number in args]


print(power_numbers(1, 2, 5, 7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 == 1, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
        

# print(filter_numbers([1, 2, 3], ODD))
# print(filter_numbers([2, 1, 3, 5, 4], EVEN))
# print(filter_numbers([1,2,3,4,5,6,7], PRIME))

